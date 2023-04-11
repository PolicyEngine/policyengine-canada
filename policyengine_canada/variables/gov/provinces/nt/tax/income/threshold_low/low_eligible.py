from policyengine_canada.model_api import *


class ntltc_low_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Low eligible income for the NTLTX"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.threshold_low
        income = Household("income", period)

        return p.low.low_base >= income