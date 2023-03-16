from policyengine_canada.model_api import *


class base_component_reduction(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit base component reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.benefits.acfb.base_component
        income = household("adjusted_family_net_income", period)
        base = household("base_component_base", period)
        return max_(0, base - p.reduction.calc(income))
