from policyengine_canada.model_api import *


class ntcb_younger_base(Variable):
    value_type = float
    entity = Household
    label = "Base income level for all middle income"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit.threshold_low
        income = Household("income", period)

        return (
            p.low.low_threshold > income >= p.high.high_threshold
        )