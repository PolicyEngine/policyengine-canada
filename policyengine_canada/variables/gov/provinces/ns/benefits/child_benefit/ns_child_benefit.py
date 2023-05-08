from policyengine_canada.model_api import *


class ns_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia Child Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        children = household("ns_child_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.ns.benefits.child_benefit
        income = household("adjusted_family_net_income", period)
        eligible = income < p.upper_threshold
        # In the lower income bracket, the families are eligible to receive
        # $1,275 per child.
        lower_income_amount = children * p.base
        # In the higher income bracket, families are eligible to receive
        # $1,275 for the first born child.
        higher_income_base = p.base * (children > 0)
        # In the higher income bracket, families are eligible to receive
        # $637.50 for each child after the first born.
        higher_income_additional_child = max_(
            0, p.higher_income_base * (children - 1)
        )
        amount_if_eligible = where(
            income < p.lower_threshold,
            lower_income_amount,
            higher_income_base + higher_income_additional_child,
        )
        return where(eligible, amount_if_eligible, 0)
