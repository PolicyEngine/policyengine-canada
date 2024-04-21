from policyengine_canada.model_api import *


class ab_base_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Alberta basic personal amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-23e.pdf"
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        return parameters(period).gov.provinces.ab.tax.income.credits.basic_personal_amount.amount
