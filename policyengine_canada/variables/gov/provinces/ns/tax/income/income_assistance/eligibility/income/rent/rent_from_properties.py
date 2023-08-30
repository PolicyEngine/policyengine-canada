from policyengine_canada.model_api import *


class rent_from_properties(Variable):
    value_type = float
    entity = Person
    label = "Rent collected from properties"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS