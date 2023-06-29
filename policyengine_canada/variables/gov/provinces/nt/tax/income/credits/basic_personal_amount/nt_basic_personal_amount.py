from policyengine_canada.model_api import *

class nt_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories basic personal amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nt.tax.income.credits.basic_personal_amount
        return p.base