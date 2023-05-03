from policyengine_canada.model_api import *


class nu_child_benefit_base_component_reduction(Variable):
    value_type = float
    entity = Household
    label = "Nunvaut child benefit base component reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.nu.tax.benefits.nucb.base
        return p.phase_out_rate.calc(income)
