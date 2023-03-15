from policyengine_canada.model_api import *


class gis_topup_reduction(Variable):
    value_type = float
    entity = Person
    label = "Guaranteed Income Supplement Top-up Reduction"
    unit = CAD
    documentation = "The amount reduced from a person's maximum GIS top-up, based on income."
    definition_period = YEAR

    def formula(person, period, parameters):
        gis_spa_category = person("gis_spa_category", period)
        gis_spa_categories = gis_spa_category.possible_values
        oas_eligible = person("oas_eligible", period)
        individual_net_income = person("individual_net_income", period)
        p = parameters(period).gov.cra.benefits.gis_spa.topup_reduction
        return select(
            [
                gis_spa_category == gis_spa_categories.SINGLE_WITH_OAS,
                gis_spa_category == gis_spa_categories.WIDOW_SPA_ELIGIBLE,
                gis_spa_category == gis_spa_categories.COUPLE_BOTH_OAS,
                (
                    gis_spa_category
                    == gis_spa_categories.COUPLE_ONE_OAS_SPA_ELIGIBLE
                ),
                (
                    gis_spa_category
                    == gis_spa_categories.COUPLE_ONE_OAS_SPA_INELIGIBLE
                )
                & oas_eligible,  # the oas_eligible makes sure this person is the eligible one in the couple, since both people in the couple will have the same category.
            ],
            [
                p.singles.calc(individual_net_income),
                p.singles.calc(individual_net_income),
                p.married.calc(individual_net_income),
                p.married.calc(individual_net_income),
                p.married.calc(individual_net_income),
            ],
            default=0,
        )
