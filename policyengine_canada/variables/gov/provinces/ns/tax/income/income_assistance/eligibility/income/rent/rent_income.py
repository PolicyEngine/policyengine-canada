from policyengine_canada.model_api import *


class rent_income(Variable):
    value_type = float
    entity = Person
    label = "Rent income"
    unit = CAD
    documentation = "Money received from the rental or leasing of property"
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
