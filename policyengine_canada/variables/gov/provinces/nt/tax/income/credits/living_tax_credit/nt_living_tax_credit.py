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
        lower = person("nt_ltc_lower_threshold", period)
        middle = person("nt_ltc_middle_threshold", period)
        higher = person("nt_ltc_higher_threshold", period)

        return min_(lower + middle + higher, p.max_amount)
