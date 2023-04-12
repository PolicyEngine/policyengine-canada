from policyengine_canada.model_api import *


class nt_ltc_middle_threshold(Variable):
    value_type = float
    entity = Person
    label = "Middle income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.living_tax_credit
        net_income = Person("individual_net_income", period)
        eligible = (p.threshold.middle.base < net_income) & (p.threshold.high.base >= net_income)

        return (
            (net_income - p.threshold.middle.base) * p.threshold.middle.rate * eligible + p.threshold.middle.supplement
        )