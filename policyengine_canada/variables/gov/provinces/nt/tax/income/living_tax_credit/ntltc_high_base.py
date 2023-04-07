from policyengine_canada.model_api import *


class ntltc_high_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount for high income under the NTLTC"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit.income_threshold
        income = household("ntltc_high_base", period)
        return (
            (income - 48_000) * 0.001 + 762
        )