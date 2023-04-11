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
        return eligible * where(
            income < p.lower_threshold,
            children * p.base,
            (
                (p.base * (children > 0))
                + (p.higher_income_base * (children - 1))
            ),
        )
