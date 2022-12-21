from policyengine_canada.model_api import *


class cwb_disability_supplement_phase_out(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit disability supplement phase out"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.cra.benefits.cwb.phase_out.disability_supplement
        category = household("cwb_disability_category", period)
        categories = category.possible_values
        return select(
            [
                category == categories.FAMILY_WITH_TWO_DISABLED_SPOUSES,
                category == categories.FAMILY_WITH_ONE_DISABLED_SPOUSE,
                category == categories.SINGLE,
            ],
            [
                p.family_with_two_spouses_disabled.calc(income),
                p.family_with_one_spouse_disabled.calc(income),
                p.single.calc(income),
            ],
            default=0,
        )
