from policyengine_canada.model_api import *


class ns_asset_limit(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia income assistance applicable asset amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    defined_for = ProvinceCode.NS
    
    def formula(household, period, parameters):
        household_size = household("household_size",period)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.assets
        return p.max_assets.calc(household_size)
