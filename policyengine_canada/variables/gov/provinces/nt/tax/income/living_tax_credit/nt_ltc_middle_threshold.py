from policyengine_canada.model_api import *


class ntltc_high_base(Variable):
    value_type = float
    entity = Person
    label = "Middle income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit
        income = Person("nt_income_tax_before_credits", period)

        return (
            income * p.threshold.low_income_rate * (p.middle.base < income) * (p.income_threshold > income) + p.threshold.middle.supplement
        )
