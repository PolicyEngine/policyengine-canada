from policyengine_canada.model_api import *


class gst_credit_singles_boost(Variable):
    value_type = float
    entity = Household
    label = "GST Credit Additional Amount for Singles"
    unit = CAD
    documentation = " "
    definition_period = YEAR

    # Singles get an amount between 0 and 161, but single _parents_ always get the full 161.
    def formula(household, period, parameters):
        married = household("is_married", period)
        single_parent_household = household(
            "gst_credit_single_parent_household", period
        )
        net_income = household("household_net_income", period)
        params = parameters(period).gov.cra.tax.income.credits.gst_credit
        threshold = params.singles_boost_threshold
        difference = max(net_income - threshold, 0)

        if single_parent_household:
            return params.singles_boost_max
        else:
            return numpy.around(
                min(difference * 0.02, params.singles_boost_max) * ~married, 2
            )
