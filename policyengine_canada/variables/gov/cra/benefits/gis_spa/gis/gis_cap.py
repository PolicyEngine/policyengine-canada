from policyengine_canada.model_api import *

class gis_cap(Variable):
    value_type = float
    entity = Person
    label = "Guaranteed Income Supplement Maximum Amount"
    unit = CAD
    documentation = "The highest GIS amount an individual could receive, based on the number of pensioners in the household, before the amount is reduced based on income. Equivalent of imgismax in the SPSD/M variable guide."
    definition_period = YEAR

    def formula(person, period, parameters):
        gis_spa_category = person("gis_spa_category", period)
        gis_spa_categories = gis_spa_category.possible_values
        oas_eligible = person("oas_eligible", period)
        p = parameters(period).gov.cra.benefits.gis_spa.gis_cap
        return select(
             [
                 gis_spa_category == gis_spa_categories.SINGLE_WITH_OAS,
                 gis_spa_category == gis_spa_categories.COUPLE_BOTH_OAS,
                 (gis_spa_category == gis_spa_categories.COUPLE_ONE_OAS_SPA_ELIGIBLE) & oas_eligible,  # the oas_eligible makes sure this person is the eligible one in the couple, since both people in the couple will have the same category.
                 (gis_spa_category == gis_spa_categories.COUPLE_ONE_OAS_SPA_INELIGIBLE) & oas_eligible
             ],
             [
                 p.one_pensioner,
                 p.two_pensioners,
                 p.two_pensioners,
                 p.one_pensioner
             ],
             default=0,
        )
