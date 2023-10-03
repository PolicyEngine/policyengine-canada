from policyengine_canada.model_api import *


class ns_income_assistance_applicable_assets(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia income assistance applicable assets"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS

    adds = "gov.provinces.ns.tax.income.income_assistance.eligibility.assets.applicable_assets"

    # None of the following is an applicable asset, per https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC3_25
