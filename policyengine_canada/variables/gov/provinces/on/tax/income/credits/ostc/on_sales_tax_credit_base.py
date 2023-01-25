from policyengine_canada.model_api import *


class on_sales_tax_credit_base(Variable):
    value_type = float
    entity = Household
    label = "Ontario Sales Tax Credit Base"
    unit = CAD
    documentation = (
        "Base amount of Ontario sales tax credits before reduction."
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        members = household("household_size", period)
        province = household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        p = parameters(period).gov.provinces.on.tax.income.credits.ostc
        amount_if_eligible = members * p.amount
        return in_ontario * amount_if_eligible
