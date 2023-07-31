from policyengine_canada.model_api import *


class ns_income_assistance_asset_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Nova Scotia income assistance asset eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        household_size = household("household_size", period)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.assets
        asset_limit = p.max_assets.calc(household_size)
        assets = household("ns_applicable_assets", period)
        return asset_limit >= assets
