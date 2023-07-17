from policyengine_canada.model_api import *


class is_infirm_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan Caregiver Amount Infirm Dependant"
    documentation = "Whthere your spouse's or common-law partner's dependant is an infirm dependant or not."
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK