from policyengine_canada.model_api import *


class rent_from_roomers(Variable):
    value_type = float
    entity = Person
    label = "rent income from roomers living"
    unit = CAD
    documentation = "rent income received from roomers living"
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
