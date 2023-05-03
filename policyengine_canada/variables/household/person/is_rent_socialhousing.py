from policyengine_canada.model_api import *


class is_rent_socialhousing(Variable):
    value_type = bool
    entity = Person
    label = "Rent Under Program"
    unit = CAD
    documentation = "whether the rent is from social housing program or not"
    definition_period = YEAR