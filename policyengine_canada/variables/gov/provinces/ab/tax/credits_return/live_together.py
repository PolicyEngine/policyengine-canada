from policyengine_canada.model_api import *


class live_together(Variable):
    value_type = bool
    entity = Person
    label = "Albert Caregiver Dependant"
    documentation = "Whthere your spouse's or common-law partner's dependant lives with you or not."
    definition_period = YEAR
    reference = "chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-23e.pdf"
    defined_for = ProvinceCode.AB
