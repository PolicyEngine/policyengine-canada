from policyengine_canada.model_api import *

class gis_reduction(Variable):
    value_type = float
    entity = Person
    label = "Guaranteed Income Supplement Reduction"
    unit = CAD
    documentation = "The amount by which the base GIS is reduced, based on personal net income and the number of pensioners in the household. Equivalent of imgismax in the SPSD/M variable guide."
    definition_period = YEAR

    def formula(person, period, parameters):
        gis_spa_category = person("gis_spa_category", period)
        gis_spa_categories = gis_spa_category.possible_values
        individual_net_income = person("individual_net_income", period)
        household = person.household
        spouse_net_income = household("spouse_net_income", period)
        gis_base = person("gis_cap", period)
        p = parameters(period).gov.cra.benefits.gis_spa.gis_reduction
        
        reduction = select(
             [
                 gis_spa_category == gis_spa_categories.SINGLE_WITH_OAS,
                 gis_spa_category == gis_spa_categories.COUPLE_BOTH_OAS,
                 (gis_spa_category == gis_spa_categories.COUPLE_ONE_OAS_SPA_ELIGIBLE) & (gis_base > 0),  # the gis_base > 0 makes sure this person is the eligible one in the couple, since both people in the couple will have the same category.
                 (gis_spa_category == gis_spa_categories.COUPLE_ONE_OAS_SPA_INELIGIBLE) & (gis_base > 0)
             ],
             [
                 p.one_pensioner.calc(individual_net_income),
                 p.two_pensioners.calc(individual_net_income + spouse_net_income),
                 p.two_pensioners.calc(individual_net_income + spouse_net_income),
                 p.one_pensioner.calc(individual_net_income)
             ],
             default=0,
        )

        return(reduction)


