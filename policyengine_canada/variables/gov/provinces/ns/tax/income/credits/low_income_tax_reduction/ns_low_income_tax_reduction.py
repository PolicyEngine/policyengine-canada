from policyengine_canada.model_api import *


class ns_low_income_tax_reduction(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia low income tax reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        base = household("ns_low_income_tax_reduction_base", period)
        children = household(
            "ns_low_income_tax_reduction_base_children", period
        )
        reduction = household("ns_low_income_tax_reduction_reduction", period)
        return max_(0, (base + children) - reduction)
