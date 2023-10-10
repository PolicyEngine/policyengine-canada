from policyengine_canada.model_api import *


class ns_rent_from_boarders(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia rent collected from boarders"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        is_dependant = person("is_dependant", period)
        return where (is_dependant, 0, ns_rent_from_boarders)