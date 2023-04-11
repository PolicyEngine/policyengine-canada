from policyengine_canada.model_api import *


class ntltc_high_eligible(Variable):
    value_type = bool
    entity = Household
    label = "High eligible income for the NTLTX"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income
        income = Household("income", period)

        return p.threshold_high.base > income >= p.threshold_low.middle.middle_base