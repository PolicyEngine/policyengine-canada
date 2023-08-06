from policyengine_canada.model_api import *


class mb_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba basic personal amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1mb/td1mb-23e.pdf" #page=1
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        is_head = person("is_head", period)
        p = parameters(period).gov.provinces.mb.credits
        return is_head * p.basic_personal_amount
