from policyengine_canada.model_api import *


class nt_living_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Max for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.living_tax_credit
        net_income = Person("individual_net_income", period)
        lower = p.threshold.middle.base * p.threshold.low_income_rate
        middle = (p.threshold.high.base - p.threshold.middle.base) * p.threshold.middle.rate + p.threshold.middle.supplement
        higher = (net_income - p.income_threshold) * p.threshold.high.rate + p.threshold.high.supplement

        return (
            min_(lower + middle + higher, p.max_amount)
        )
