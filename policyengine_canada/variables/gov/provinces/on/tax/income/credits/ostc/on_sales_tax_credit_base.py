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
    defined_for = ProvinceCode.ONT

    def formula(household, period, parameters):
        members = household("household_size", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.ostc
        return members * p.amount
