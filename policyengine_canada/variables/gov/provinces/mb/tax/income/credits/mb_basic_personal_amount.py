from policyengine_canada.model_api import *


class mb_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba basic personal amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1mb/td1mb-23e.pdf"
    defined_for = ProvinceCode.MB

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.mb.credits
        return p.basic_personal_amount