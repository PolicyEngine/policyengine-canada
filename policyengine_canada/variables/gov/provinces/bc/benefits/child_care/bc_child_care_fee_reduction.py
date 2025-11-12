from policyengine_canada.model_api import *


class bc_child_care_fee_reduction(Variable):
    value_type = float
    entity = Household
    label = "BC Child Care Fee Reduction Initiative"
    documentation = "Fee reduction for families at participating BC child care facilities (not income-tested)"
    unit = CAD
    definition_period = YEAR  # Annual total of monthly fee reductions
    defined_for = ProvinceCode.BC
    reference = "https://www2.gov.bc.ca/gov/content/family-social-supports/caring-for-young-children/childcarebc-programs/child-care-fee-reduction-initiative-provider-opt-in-status"

    def formula(household, period, parameters):
        # This benefit is available to all families with children 12 and under
        # at participating facilities (not income-tested)
        p = parameters(
            period
        ).gov.provinces.bc.benefits.child_care_fee_reduction

        person = household.members
        age = person("age", period)

        # Eligible children are 12 and under
        is_eligible = age <= p.max_age

        # Maximum monthly fee reduction amounts by age group
        # Simplified to use main age categories
        monthly_reduction = where(
            age < 3,  # Infant/toddler
            p.max_reduction.infant_toddler,
            where(
                age < 5,  # Preschool (3-5)
                p.max_reduction.preschool,
                where(
                    age <= 12,  # School age (5-12)
                    p.max_reduction.school_age,
                    0,
                ),
            ),
        )

        # Annual reduction = monthly reduction * 12 months * eligible
        annual_reduction_per_child = monthly_reduction * 12 * is_eligible

        # Sum across all children
        return household.sum(annual_reduction_per_child)
