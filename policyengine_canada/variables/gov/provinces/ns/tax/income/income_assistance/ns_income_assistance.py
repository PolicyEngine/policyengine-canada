from policyengine_canada.model_api import *


class ns_income_assistance(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia Income Assistance"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS
