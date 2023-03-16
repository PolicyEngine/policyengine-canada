from policyengine_canada.model_api import *


class working_component_reduction(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit working component reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.benefits.acfb.working_component
        income = household("adjusted_family_net_income", period)
        base = household("working_component_phase_in", period)
        return max_(0, base - p.reduction.calc(income))
