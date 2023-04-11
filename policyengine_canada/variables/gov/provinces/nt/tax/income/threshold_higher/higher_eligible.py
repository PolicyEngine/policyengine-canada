from policyengine_canada.model_api import *


class ntltc_higher_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Higher eligible income for the NTLTX"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.threshold_high
        income = Household("income", period)

        return p.base <= income