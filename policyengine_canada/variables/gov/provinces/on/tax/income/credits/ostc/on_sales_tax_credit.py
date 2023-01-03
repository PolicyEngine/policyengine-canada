from policyengine_canada.model_api import *


class on_sales_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Ontario sales tax credits"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        base = household("on_sales_tax_credit_base", period)
        reduction = household("on_sales_tax_credit_reduction", period)
        return max_(0, base - reduction)
