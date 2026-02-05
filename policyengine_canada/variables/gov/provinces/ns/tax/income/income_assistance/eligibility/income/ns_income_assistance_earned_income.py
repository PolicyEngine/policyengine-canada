from policyengine_canada.model_api import *


class ns_income_assistance_earned_income (Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia income assistance earned income"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS

    adds = "gov.provinces.ns.tax.income.income_assistance.eligibility.income.earned_income"