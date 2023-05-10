from policyengine_canada.model_api import *


class ns_low_income_tax_reduction_reduction(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia low income tax reduction reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        return parameters(
            period
        ).gov.provinces.ns.tax.income.credits.low_income_tax_reduction.phase_out.calc(
            income
        )
