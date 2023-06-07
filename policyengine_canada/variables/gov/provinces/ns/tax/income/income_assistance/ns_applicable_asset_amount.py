from policyengine_canada.model_api import *


class ns_applicable_asset_amount(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia income assistance applicable asset amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    defined_for = ProvinceCode.NS
    
    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.assets
        return add(household, period, p.applicable_assets)
