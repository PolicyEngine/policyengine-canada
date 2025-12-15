from policyengine_canada.model_api import *


class gis_reduction_spa_couple(Variable):
    value_type = float
    entity = Person
    label = "Guaranteed Income Supplement Reduction for a Recipient with SPA-eligible Spouse"
    unit = CAD
    documentation = "The amount by which the base GIS is reduced, based on personal net income and the number of pensioners in the household. This is implemented as a variable, not a parameter, due to the complexity and dependencies of the reduction rate."
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        gis_spa_category = person("gis_spa_category", period)
        gis_spa_categories = gis_spa_category.possible_values
        gis_income = person("gis_income", period)
        spouse_gis_income = household("spouse_gis_income", period)
        combined_gis_income = gis_income + spouse_gis_income
        state = person.state
        crossover = state("gis_spa_crossover", period)
        breakeven_spa_eligible = state("breakeven_spa_eligible", period)
        breakeven_spa_ineligible = state("breakeven_spa_ineligible", period)
        plateau_range = breakeven_spa_eligible - crossover
        p = parameters(period).gov.cra.benefits.gis_spa.gis_reduction

        # Reduce like other pensioner couples up to the crossover point
        first_part = min(
            p.two_pensioners.calc(combined_gis_income),
            p.two_pensioners.calc(crossover),
        )
        # Plateau until the spouse's SPA-gis-portion is exhausted, as captured by the variable plateau_range. The first part must be maxed-out for this to be non-zero.
        second_part = min(
            (combined_gis_income - first_part) * p.gis_spa_couple_plateau_rate,
            plateau_range * p.gis_spa_couple_plateau_rate,
        ) * (first_part == (p.two_pensioners.calc(crossover)))
        # Start reducing again at the married couple breakeven point for income beyond the crossover maximum. Only be non-zero if there's any income in that range.
        third_part = p.two_pensioners.calc(
            combined_gis_income - (crossover - 48) - plateau_range
        ) * ((combined_gis_income > (crossover - plateau_range)))

        #   return(third_part)
        return (first_part + second_part + third_part) * (
            gis_spa_category == gis_spa_categories.COUPLE_ONE_OAS_SPA_ELIGIBLE
        )
