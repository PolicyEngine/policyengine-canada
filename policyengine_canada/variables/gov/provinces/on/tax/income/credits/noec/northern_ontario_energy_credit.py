from policyengine_canada.model_api import *


class northern_ontario_energy_credit(Variable):
    value_type = float
    entity = Household
    label = "Northern ontario energy credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "is_in_northern_ontario"

    def formula(household, period, parameters):
        person = household.members
        age = person("age", period)
        married = household("is_married", period)
        children = household("count_children", period)
        category = household("oeptc_category", period)
        afni = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.noec
        # subtarct base amount from afni (varies by category)
        excess = max_(afni - p.phase_out.start[category], 0)
        phase_out = excess * p.multiplier
        # subtract the excess amount from the base noec amount
        phased_out = p.base[category] - phase_out
        # single with shared custody household calculation continues - phased-out devided by 2
        shared_custody_phased_out_divided = (
            phased_out / p.phase_out.shared_custody.divisor
        )
        # second phase out process - same steps as previously with different amounts
        shared_custody_excess = max_(
            afni - p.phase_out.shared_custody.start, 0
        )
        shared_custody_second_phase_out = shared_custody_excess * p.multiplier
        shared_custody_second_phased_out = (
            p.phase_out.shared_custody.base - shared_custody_second_phase_out
        )
        shared_custody_second_phased_out_divided = (
            shared_custody_second_phased_out
            / p.phase_out.shared_custody.divisor
        )
        # single with shared custody household afni under 43_602 amount is 205.50
        shared_custody_result = where(
            afni > p.phase_out.start[category],
            shared_custody_phased_out_divided
            + shared_custody_second_phased_out_divided,
            p.phase_out.shared_custody.base,
        )
        eligible = (age >= p.age_eligibility) | married | (children > 0)
        return eligible * max_(
            0,
            where(
                category == category.possible_values.SINGLE_SHARED_CUSTODY,
                shared_custody_result,
                phased_out,
            ),
        )
