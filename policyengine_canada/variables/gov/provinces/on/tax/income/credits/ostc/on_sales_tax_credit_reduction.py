from policyengine_canada.model_api import *


class on_sales_tax_credit_reduction(Variable):
    value_type = float
    entity = Household
    label = "Ontario Sales Tax Credit reduction"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        family = household("household_size", period) > 1
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.ostc.reduction
        return where(family, p.family.calc(income), p.single.calc(income))
