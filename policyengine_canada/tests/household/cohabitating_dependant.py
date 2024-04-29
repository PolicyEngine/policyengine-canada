from policyengine_canada.model_api import *


class cohabitating_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Dependant living with the head of household"
    documentation = "Whthere your spouse's or common-law partner's dependant lives with you or not."
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-23e.pdf#page=1"