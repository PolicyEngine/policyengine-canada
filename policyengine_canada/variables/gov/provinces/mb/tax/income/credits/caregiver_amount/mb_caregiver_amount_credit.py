from policyengine_canada.model_api import *


class mb_caregiver_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba caregiver amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.caregiver_amount
        
        caregiver = person("is_caregiver", period)

        return caregiver * person("mb_dependent_credit_amount", period)