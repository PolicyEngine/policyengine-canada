from policyengine_canada.model_api import *


class in_need_of_protective_services(Variable):
    value_type = bool
    entity = Person
    label = "Person is in need of protective services"
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC3_8"
    )
