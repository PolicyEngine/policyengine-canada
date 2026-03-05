from policyengine_canada.model_api import *


class bc_child_care_fee_reduction(Variable):
    value_type = float
    entity = Household
    label = "BC Child Care Fee Reduction Initiative"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    reference = (
        "https://www2.gov.bc.ca/gov/content/family-social-supports/caring-for-young-children/childcarebc-programs/child-care-fee-reduction-initiative-provider-opt-in-status",
        "https://www2.gov.bc.ca/assets/gov/family-and-social-supports/child-care/childcarebc-programs/ccfri/ccfri_funding_guidelines_24_25.pdf#page=5",
    )

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.bc.benefits.child_care_fee_reduction

        person = household.members
        age = person("age", period)
        is_family = person("is_family_child_care", period)

        is_eligible = age <= p.max_age

        # Age boundaries per CCFRI Funding Guidelines Table 1
        preschool_age = p.age.preschool
        kindergarten_age = p.age.kindergarten
        school_age_start = p.age.school_age

        is_infant_toddler = age < preschool_age
        is_preschool = (age >= preschool_age) & (age < kindergarten_age)
        is_kindergarten = (age >= kindergarten_age) & (age < school_age_start)
        is_school_age = (age >= school_age_start) & is_eligible

        # Group care rates (default)
        group_reduction = select(
            [
                is_infant_toddler,
                is_preschool,
                is_kindergarten,
                is_school_age,
            ],
            [
                p.max_reduction.group.infant_toddler,
                p.max_reduction.group.preschool,
                p.max_reduction.group.kindergarten,
                p.max_reduction.group.school_age,
            ],
            default=0,
        )

        # Family/in-home multi-age care rates
        family_reduction = select(
            [
                is_infant_toddler,
                is_preschool,
                is_kindergarten,
                is_school_age,
            ],
            [
                p.max_reduction.family.infant_toddler,
                p.max_reduction.family.preschool,
                p.max_reduction.family.kindergarten,
                p.max_reduction.family.school_age,
            ],
            default=0,
        )

        monthly_reduction = where(is_family, family_reduction, group_reduction)
        annual_reduction_per_child = monthly_reduction * 12
        return household.sum(annual_reduction_per_child)
