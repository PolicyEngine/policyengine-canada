from policyengine_canada.model_api import *


class bc_affordable_child_care_benefit(Variable):
    value_type = float
    entity = Household
    label = "BC Affordable Child Care Benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    reference = (
        "https://www2.gov.bc.ca/gov/content/family-social-supports/caring-for-young-children/childcarebc-programs/child-care-benefit",
        "https://www2.gov.bc.ca/gov/content/family-social-supports/caring-for-young-children/childcarebc-programs/child-care-benefit/information-for-families/rates-payments",
    )

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.bc.benefits.child_care

        # Family size adjustment: per member beyond base count
        income = household("adjusted_family_net_income", period)
        household_size = household("household_size", period)
        family_size_adjustment = (
            max_(0, household_size - p.base_family_size) * p.family_size_adjustment
        )
        adjusted_income = max_(0, income - family_size_adjustment)

        eligible = adjusted_income <= p.income_limit

        person = household.members
        age = person("age", period)

        # Age boundaries per ACCB rate schedule
        toddler_age = p.age.toddler
        preschool_age = p.age.preschool
        school_age_start = p.age.school_age
        max_age = p.age.max_age

        is_under_19_months = age < toddler_age
        is_toddler = (age >= toddler_age) & (age < preschool_age)
        is_preschool = (age >= preschool_age) & (age < school_age_start)
        is_school_age = (age >= school_age_start) & (age < max_age)

        monthly_benefit = select(
            [is_under_19_months, is_toddler, is_preschool, is_school_age],
            [
                p.max_amount.under_19_months,
                p.max_amount.age_19_to_36_months,
                p.max_amount.preschool_age,
                p.max_amount.school_age,
            ],
            default=0,
        )

        # Income phase-out above max benefit threshold
        max_benefit_threshold = p.max_benefit_income_threshold
        excess_income = max_(0, adjusted_income - max_benefit_threshold)
        phase_out_range = p.income_limit - max_benefit_threshold
        phase_out_fraction = excess_income / phase_out_range
        benefit_rate = where(
            adjusted_income <= max_benefit_threshold,
            1.0,
            max_(0, 1 - phase_out_fraction),
        )

        annual_benefit_per_child = monthly_benefit * 12 * benefit_rate
        total_benefit = household.sum(annual_benefit_per_child)

        return where(eligible, total_benefit, 0)
