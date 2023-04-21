from policyengine_canada.model_api import *


class cce_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        income = household(
            "household_market_income", period
        )  # !! not sure if family income is the household_market_income
        eligible = household("cce_eligible_child", period)
        return eligible * (p.rate * income)


# todo: limit credit
