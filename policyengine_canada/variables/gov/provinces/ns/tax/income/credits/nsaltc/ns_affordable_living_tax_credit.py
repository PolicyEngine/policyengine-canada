from policyengine_canada.model_api import *


class ns_affordable_living_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia affordable living tax credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("count_children", period)
        p = parameters(period).gov.provinces.ns.tax.income.credits.nsaltc
        return max_(0, (p.individual_base + (p.child_base * children) ) - p.reduction.calc(income))

