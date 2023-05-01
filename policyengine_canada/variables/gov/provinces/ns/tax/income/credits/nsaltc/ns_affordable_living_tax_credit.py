from policyengine_canada.model_api import *


class ns_affordable_living_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "NSALTC"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("count_children", period)
        p = parameters(period).gov.provinces.ns.tax.income.credits.nsaltc
        child_amount = p.child_base * children
        max_amount = p.individual_base + child_amount
        reduction = p.reduction.calc(income)
        return max_(max_amount - reduction, 0)
