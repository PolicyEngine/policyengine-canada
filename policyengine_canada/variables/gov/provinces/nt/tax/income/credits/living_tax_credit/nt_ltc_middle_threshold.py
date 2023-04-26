from policyengine_canada.model_api import *


class nt_ltc_middle_threshold(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories middle income for cost of living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.living_tax_credit
        net_income = person("individual_net_income", period)
        eligible = (
            p.threshold.middle.base < net_income <= p.threshold.high.base
        )

        return eligible * (
            (net_income - p.threshold.middle.base) * p.threshold.middle.rate
            + p.threshold.middle.supplement
        )
