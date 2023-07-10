from policyengine_canada.model_api import *


class dependant_age(Variable):
    value_type = int
    entity = Person
    label = "Saskatchewan Caregiver Amount"
    unit = YEAR
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK