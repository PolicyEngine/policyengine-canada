from policyengine_canada.model_api import *


class ntltc_high_base(Variable):
    value_type = float
    entity = Person
    label = "Higher income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.living_tax_credit
        net_income = Person("individual_net_income", period)
        eligible = (p.threshold.high.base < net_income) & (net_income < p.income_threshold)

        return (
            (net_income - p.threshold.high.base) * p.threshold.high.rate * eligible + p.threshold.high.supplement
        )