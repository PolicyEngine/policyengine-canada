from policyengine_canada.model_api import *


class nt_ltc_higher_threshold(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories higher income for cost of living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.living_tax_credit
        net_income = person("individual_net_income", period)
        eligible = p.threshold.high.base < net_income

        return eligible * (
            (net_income - p.threshold.high.base) * p.threshold.high.rate
            + p.threshold.high.supplement
        )
