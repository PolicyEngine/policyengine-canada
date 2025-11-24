from policyengine_canada.model_api import *


class government_financial_assistance_payments(Variable):
    value_type = float
    entity = Person
    label = "Government financial assistance payments"
    unit = CAD
    documentation = (
        "Income from financial assistance provided by the government"
    )
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
