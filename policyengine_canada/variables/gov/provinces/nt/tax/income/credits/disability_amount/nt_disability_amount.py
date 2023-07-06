from policyengine_canada.model_api import *


class nt_disability_amount(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Disability Amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    adds = "gov.provinces.nt.tax.income.credits.disability_amount.base"
