from policyengine_canada.model_api import *


class mb_infirm_dependant_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba infirm dependant dependant amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.infirm_dependant_amount

        caregiver = person("is_caregiver", period)

        return caregiver * person("mb_dependant_eligibility", period)