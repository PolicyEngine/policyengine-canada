from policyengine_canada.model_api import *


class sk_housing_benefit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Housing Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        eligible = household("sk_housing_benefit_eligible", period)
        income = household("adjusted_family_net_income", period)
        person = household.members
        rent = person("rent", period)
        household_rent = household.sum(rent)
        dependants = household("count_dependants", period)
        utility_costs = household("utilities_costs", period)
        precentage_spend_housing = (household_rent + utility_costs) / income
        p = parameters(period).gov.provinces.sk.benefits.housing_benefit

        shelter_costs_lower_bracket = (
            p.amount.higher_threshold.threshold
            >= precentage_spend_housing
            >= p.amount.lower_threshold.threshold
        )
        shelter_costs_higher_bracket = (
            precentage_spend_housing > p.amount.higher_threshold.threshold
        )
        # If a household spends between 45% and 35% of their income on housing expenditures
        # it is eligible for a benefit amount depending on the number of dependants
        lower_bracket_amount = shelter_costs_lower_bracket * (
            select(
                [dependants == 0, dependants == 1, dependants >= 2],
                [
                    p.amount.lower_threshold.no_dependants,
                    p.amount.lower_threshold.one_dependants,
                    p.amount.lower_threshold.two_or_more_dependants,
                ],
            )
        )
        # If a household spends over 45% of their income on housing expenditures
        # it is eligible for a higher benefit amount depending on the number of dependants
        higher_bracket_amount = shelter_costs_higher_bracket * (
            select(
                [dependants == 0, dependants == 1, dependants >= 2],
                [
                    p.amount.higher_threshold.no_dependants,
                    p.amount.higher_threshold.one_dependants,
                    p.amount.higher_threshold.two_or_more_dependants,
                ],
            )
        )

        sk_housing_benefit = eligible * (
            higher_bracket_amount + lower_bracket_amount
        )
        return sk_housing_benefit
