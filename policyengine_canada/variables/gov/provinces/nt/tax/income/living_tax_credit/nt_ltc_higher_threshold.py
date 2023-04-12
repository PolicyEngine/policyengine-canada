from policyengine_canada.model_api import *


class nt_ltc_higher_threshold(Variable):
    value_type = float
    entity = Person
    label = "Higher income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit
        income = Person("individual_net_income", period)

        return (
            p.max_amount * (p.income_threshold <= income) + p.threshold.high.supplement
        )