from policyengine_canada.model_api import *


class ns_income_assistance_applicable_asset(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia Income Assistance applicable asset"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    defined_for = ProvinceCode.NS
    adds = ["total_individual_pre_tax_income"]
