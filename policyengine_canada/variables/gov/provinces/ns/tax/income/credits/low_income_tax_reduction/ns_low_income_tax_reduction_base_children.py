from policyengine_canada.model_api import *


class ns_low_income_tax_reduction_base_children(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia low income tax reduction base for children"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.low_income_tax_reduction
        children = household(
            "ns_low_income_tax_reduction_eligible_children", period
        )
        return children * p.base.dependant.base
