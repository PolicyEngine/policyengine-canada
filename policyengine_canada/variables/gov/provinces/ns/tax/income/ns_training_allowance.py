from policyengine_canada.model_api import *


class ns_training_allowance(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia training allowance"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    defined_for = ProvinceCode.NS
