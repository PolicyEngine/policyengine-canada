from policyengine_canada.model_api import *


class ns_low_income_tax_reduction_reduction(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia low income tax reduction reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.low_income_tax_reduction.phase_out
        income = household("adjusted_family_net_income", period)
        return max_(0, income - p.start) * p.rate
