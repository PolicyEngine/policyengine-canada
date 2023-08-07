from policyengine_canada.model_api import *


class education_property_tax_received(Variable):
    value_type = float
    entity = Person
    label = "Education property taxes received"
    unit = CAD
    definition_period = YEAR
