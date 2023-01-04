from policyengine_canada.model_api import *

class gst_credit_singles_boost(Variable):
    value_type = float
    entity = Household
    label = "GST Credit Additional Amount for Singles"
    unit = CAD
    documentation = " "
    definition_period = YEAR

    def formula(household, period, parameters):
        married     = household("is_married", period)
        net_income  = household("household_net_income", period)
        base_amount = parameters(period).gov.cra.tax.income.credits.gst_credit.singles_boost
        difference  = max(net_income - base_amount, 0)
        
        return numpy.around(min(difference * 0.02, 161) * ~married, 2)