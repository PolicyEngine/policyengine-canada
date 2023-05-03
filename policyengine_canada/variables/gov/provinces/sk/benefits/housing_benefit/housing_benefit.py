from policyengine_canada.model_api import *


class sk_active_housing_benefit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Housing Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p1 = parameters(period).gov.provinces.sk.benefits.housing_benefit
        p2 = variables(period).household.income.household
        p3 = variables(period).household.expenses.housing

        #1 single and couples: income spend on rent and utilities = 35% to 45%
        c1 = ((p3.rent + p3.cost_on_utilities) / p2.market_income) >= p1.amount.lower_threshold.threshold
        #2 single and couples: income spend on rent and utilities > 35%

        #3 one dependant: income spend on rent and utilities = 35% to 45%

        #4 one dependant: income spend on rent and utilities > 35%

        #5 two or more dependants: income spend on rent and utilities = 35% to 45%

        #6 two or more dependants: income spend on rent and utilities > 35%


        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.sk.benefits.afb
        person = household.members
        child = person("age", period) <= p.eligibility.age
        disabled = person("is_disabled", period)
        children = household.sum(child)
        disabled_children = household.sum(child & disabled)
        non_disabled_children = children - disabled_children
        eligible = income <= p.eligibility.income
        amount_if_eligible = (
            p.amount.non_disabled * non_disabled_children
        ) + (p.amount.disabled * disabled_children)
        return eligible * amount_if_eligible
