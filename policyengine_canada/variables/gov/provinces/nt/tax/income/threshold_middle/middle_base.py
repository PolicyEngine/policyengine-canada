from policyengine_canada.model_api import *


class ntltc_middle_base(Variable):
    value_type = float
    entity = Household
    label = "Middle income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit.threshold_middle
        income = Household("income", period)

        return (
            p.middle.middle_rate * (income - p.low.low_base) + p.middle.middle_add
        )