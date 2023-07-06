from policyengine_canada.model_api import *


class nu_child_benefit_base_component_base(Variable):
    value_type = float
    entity = Household
    label = "Nunvaut child benefit base component base"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        children = household("nu_child_benefit_eligible_children", period)
        return (
            children
            * parameters(period).gov.provinces.nu.tax.benefits.nucb.base.amount
        )
