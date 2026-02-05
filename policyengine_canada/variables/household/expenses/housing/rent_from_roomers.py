from policyengine_canada.model_api import *


class rent_from_roomers(Variable):
    value_type = float
    entity = Person
    label = "Rent collected from roomers"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    
