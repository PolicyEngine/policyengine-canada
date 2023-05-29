from policyengine_canada.model_api import *


class ns_income_assistance_asset_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Nova Scotia income assistance asset eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        asset_amount = household("asset_amount", period)
        household_size = household("household_size",period)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility
        max_asset_limit = np.where(household_size == 1, p.asset_limit, p.max_asset_limit)
        return asset_amount <= max_asset_limit
