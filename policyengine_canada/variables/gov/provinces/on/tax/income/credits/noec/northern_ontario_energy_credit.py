from policyengine_canada.model_api import *


class northern_ontario_energy_credit(Variable):
    value_type = float
    entity = Household
    label = "Northern ontario energy credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        age = person("age", period)
        married = household("is_married", period)
        children = household("count_children", period)
        in_northern_ontario = household("is_in_northern_ontario", period)
        category = household("oeptc_category", period)
        afni = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.noec
        excess = max_(afni - p.phase_out.start[category], 0)
        phase_out = excess * p.multiplication_factor
        print(phase_out)
        phased_out = p.base[category] - phase_out
        shared_custody_phased_out_divided = (
            phased_out / p.phase_out.shared_custody.divisor
        )
        shared_custody_excess = max_(
            afni - p.phase_out.shared_custody.start, 0
        )
        shared_custody_second_phase_out = (
            shared_custody_excess * p.multiplication_factor
        )
        shared_custody_second_phased_out = (
            p.phase_out.shared_custody.base - shared_custody_second_phase_out
        )
        shared_custody_second_phased_out_divided = (
            shared_custody_second_phased_out
            / p.phase_out.shared_custody.divisor
        )
        # shared custody under 43_602 amount is 205.50
        shared_custody_result = where(
            afni > p.phase_out.start[category],
            shared_custody_phased_out_divided
            + shared_custody_second_phased_out_divided,
            p.phase_out.shared_custody.base,
        )
        eligible = age >= p.age_eligibility or married == True or children > 0
        return (
            eligible
            * in_northern_ontario
            * max_(
                0,
                where(
                    category == category.possible_values.SINGLE_SHARED_CUSTODY,
                    shared_custody_result,
                    phased_out,
                ),
            )
        )
