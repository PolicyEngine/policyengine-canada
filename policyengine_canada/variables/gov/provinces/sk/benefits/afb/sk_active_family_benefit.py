from policyengine_canada.model_api import *


class sk_active_family_benefit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Active Family Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
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
