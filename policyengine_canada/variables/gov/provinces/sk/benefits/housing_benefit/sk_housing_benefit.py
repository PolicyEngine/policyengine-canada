from policyengine_canada.model_api import *


class sk_housing_benefit(Variable):
    value_type = bool
    entity = Household
    label = "Saskatchewan Housing Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        eligible = household("sk_housing_benefit_eligible", period)
        income = household("adjusted_family_net_income.py", period)
        rent = household("rent", period)
        dependants = household("count_dependants",period)
        utility_costs = household("utilities_costs", period)
        precentage_spend_housing = (rent + utility_costs) / income
        p = parameters(period).gov.provinces.sk.benefits.housing_benefit

        shelter_costs_lower_bracket = precentage_spend_housing > p.amount.lower_threshold.threshold
        shelter_costs_higher_bracket = precentage_spend_housing > p.amount.higher_threshold.threshold

        lower_bracket_amount = shelter_costs_lower_bracket * (select(
            [dependants == 0, dependants == 1, dependants >= 2],
            [p.amount.lower_threshold.no_dependants,
            p.amount.lower_threshold.one_dependants,
            p.amount.lower_threshold.two_or_more_dependants])
        )

        higher_bracket_amount = shelter_costs_higher_bracket * (select(
            [
                dependants == 0, 
                dependants == 1, 
                dependants >= 2
            ],
            [
                p.amount.higher_threshold.no_dependants - p.amount.lower_threshold.no_dependants,
                p.amount.higher_threshold.one_dependants - p.amount.lower_threshold.one_dependants,
                p.amount.higher_threshold.two_or_more_dependants - p.amount.lower_threshold.two_or_more_dependants
            ]))

        return eligible * (higher_bracket_amount + lower_bracket_amount)
