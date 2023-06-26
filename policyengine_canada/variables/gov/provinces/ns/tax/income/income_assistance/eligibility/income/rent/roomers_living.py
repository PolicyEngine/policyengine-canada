from policyengine_canada.model_api import *


class roomers_living(Variable):
    value_type = bool
    entity = Person
    label = "roomers living"
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    defined_for = ProvinceCode.NS