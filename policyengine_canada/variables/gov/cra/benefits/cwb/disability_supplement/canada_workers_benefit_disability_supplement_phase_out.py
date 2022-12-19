from policyengine_canada.model_api import *


class canada_workers_benefit_disability_supplement_phase_out(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit disability supplement phase out"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household.person("adjusted_net_family_income", period)
        p = parameters(period).gov.cra.benefits.cwb
        category = household(
            "canada_workers_benefit_disability_category", period
        )
        return select(
            [
                category == FAMILY_WITH_TWO_DISABLED_SPOUSES,
                category == FAMILY_WITH_ONE_DISABLED_SPOUSE,
                category == SINGLE,
            ],
            [
                p.phase_out.disability_supplement.family_with_two_spouses_disabled.calc(
                    income
                ),
                p.phase_out.disability_supplement.family_with_one_spouse_disabled.calc(
                    income
                ),
                p.phase_out.disability_supplement.single.calc(income),
            ],
            default=0,
        )
