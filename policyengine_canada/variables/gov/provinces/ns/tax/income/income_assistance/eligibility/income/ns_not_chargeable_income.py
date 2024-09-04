from policyengine_canada.model_api import *


class ns_not_chargeable_income(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia income assistance not chargeable income"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS

    adds = "gov.provinces.ns.tax.income.income_assistance.eligibility.income.not_chargeable_income"