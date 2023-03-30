from policyengine_canada.model_api import *


class nb_low_income_tax_reduction(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick low income tax reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.low_income_tax_reduction
        income = household("adjusted_family_net_income", period)
        base = household("nb_low_income_tax_reduction_base", period)
        return max_(0, base - p.rate.calc(income))
