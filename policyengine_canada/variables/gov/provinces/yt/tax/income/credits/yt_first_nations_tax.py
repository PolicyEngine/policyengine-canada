from policyengine_canada.model_api import *


class yt_first_nations_tax(Variable):
    value_type = float
    entity = Household
    label = "Yukon first nations tax"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.first_nations_tax
        eligible = household("resides_on_settlement_land", period)
        return income * p.rate * eligible
