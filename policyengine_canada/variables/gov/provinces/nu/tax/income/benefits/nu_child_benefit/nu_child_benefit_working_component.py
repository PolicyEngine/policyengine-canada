from policyengine_canada.model_api import *


class nu_child_benefit_working_component(Variable):
    value_type = float
    entity = Household
    label = "Nunvaut child benefit working component"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        children = household("nu_child_benefit_eligible_children", period)
        income = household("family_working_income", period)
        p = parameters(period).gov.provinces.nu.tax.benefits.nucb.working
        phase_in_amount = p.phase_in_rate.calc(income)
        max_amount = p.amount.calc(children)
        return min_(phase_in_amount, max_amount)
