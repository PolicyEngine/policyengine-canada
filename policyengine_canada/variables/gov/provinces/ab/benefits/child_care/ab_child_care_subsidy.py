from policyengine_canada.model_api import *


class ab_child_care_subsidy(Variable):
    value_type = float
    entity = Household
    label = "Alberta Child Care Subsidy"
    documentation = "Income-tested subsidy to help Alberta families with child care costs (2024 income-based model, before April 2025 flat-fee changes)"
    unit = CAD
    definition_period = YEAR  # Annual total of monthly subsidies
    defined_for = ProvinceCode.AB
    reference = "https://www.alberta.ca/child-care-subsidy"

    def formula(household, period, parameters):
        # Get family income
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.ab.benefits.child_care

        person = household.members
        age = person("age", period)
        is_child = person("is_child", period)

        # Different income limits for different age groups
        # Ages 0-5 (preschool): income must be under $180,000
        # Kindergarten-Grade 6 (ages 5-12): income must be under $90,000
        preschool_age = age < 5
        school_age = (age >= 5) & (age <= 12)

        preschool_eligible = preschool_age & (
            income < p.income_limit_preschool
        )
        school_age_eligible = school_age & (income < p.income_limit_school_age)

        # Simplified monthly subsidy amounts (varies by income in reality)
        # Using base amounts - actual amounts vary by income level
        # These are average/representative amounts
        monthly_subsidy = where(
            preschool_eligible,
            p.base_subsidy.preschool,
            where(school_age_eligible, p.base_subsidy.school_age, 0),
        )

        # Apply income-based reduction for higher incomes
        # Simplified: full subsidy below threshold, linear phase-out to income limit
        income_limit = where(
            preschool_age, p.income_limit_preschool, p.income_limit_school_age
        )
        phase_out_start = income_limit * p.phase_out_start_fraction

        subsidy_rate = where(
            income <= phase_out_start,
            1.0,
            max_(
                0, (income_limit - income) / (income_limit - phase_out_start)
            ),
        )

        # Annual subsidy = monthly subsidy * 12 * subsidy_rate * eligible
        eligible = preschool_eligible | school_age_eligible
        annual_subsidy_per_child = (
            monthly_subsidy * 12 * subsidy_rate * is_child * eligible
        )

        # Sum across all children
        return household.sum(annual_subsidy_per_child)
