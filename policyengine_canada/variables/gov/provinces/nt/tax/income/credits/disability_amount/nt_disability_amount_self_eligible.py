from policyengine_canada.model_api import *


class nt_disability_amount_self_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Northwest Territories Disability Amount for self elligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        return person("is_disabled", period)
