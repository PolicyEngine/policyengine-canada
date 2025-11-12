from policyengine_canada.model_api import *


class bc_affordable_child_care_benefit(Variable):
    value_type = float
    entity = Household
    label = "BC Affordable Child Care Benefit"
    documentation = "Monthly benefit to help eligible BC families with child care costs, income-tested up to $111,000"
    unit = CAD
    definition_period = YEAR  # Annual total of monthly benefits
    defined_for = ProvinceCode.BC
    reference = "https://www2.gov.bc.ca/gov/content/family-social-supports/caring-for-young-children/childcarebc-programs/child-care-benefit"

    def formula(household, period, parameters):
        # Get adjusted family net income
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.bc.benefits.child_care

        # Family size adjustment: $2,000 per member beyond first two
        household_size = household("household_size", period)
        family_size_adjustment = (
            max_(0, household_size - 2) * p.family_size_adjustment
        )

        # Adjusted income for benefit calculation
        adjusted_income = max_(0, income - family_size_adjustment)

        # Check if income is below general eligibility threshold
        eligible = adjusted_income <= p.income_limit

        # Calculate benefit per child based on age
        person = household.members
        age = person("age", period)
        is_child = person("is_child", period)

        # Maximum monthly amounts by age (for licensed group care)
        # Convert to annual by multiplying by 12
        monthly_benefit = where(
            age < 1.583,  # Under 19 months (19/12 = 1.583 years)
            p.max_amount.under_19_months,
            where(
                age < 3,  # 19-36 months
                p.max_amount.age_19_to_36_months,
                where(
                    age < 5,  # 37 months to school age (assume 5)
                    p.max_amount.preschool_age,
                    where(
                        age < 13,  # School age
                        p.max_amount.school_age,
                        0,
                    ),
                ),
            ),
        )

        # Apply income testing - reduce benefit for incomes above threshold
        # Simplified: maximum benefit at low income, phases out to zero at upper limit
        max_benefit_threshold = p.max_benefit_income_threshold
        benefit_rate = where(
            adjusted_income <= max_benefit_threshold,
            1.0,
            max_(
                0,
                1
                - (adjusted_income - max_benefit_threshold)
                / (p.income_limit - max_benefit_threshold),
            ),
        )

        # Annual benefit = monthly benefit * 12 * benefit rate * is_child
        annual_benefit_per_child = (
            monthly_benefit * 12 * benefit_rate * is_child
        )

        # Sum across all children
        total_benefit = household.sum(annual_benefit_per_child)

        return where(eligible, total_benefit, 0)
