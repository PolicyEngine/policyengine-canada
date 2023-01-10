from policyengine_canada.model_api import *


class gst_credit_childless_boost(Variable):
    value_type = float
    entity = Household
    label = "GST Credit Additional Amount for Singles"
    unit = CAD
    documentation = "Single-adult households without children get 2 percent of the difference between family net income and the threshold amount, up to a maximum of $161. Single-adult households _with_ children always get the maximum of $161, regardless of household net income."
    definition_period = YEAR

    # Singles get an amount between 0 and 161, but single _parents_ always get the full 161.
    def formula(household, period, parameters):
        married = household("is_married", period)
        single_parent_household = household(
            "gst_credit_single_parent_household", period
        )
        net_income = household("household_net_income", period)
        p = parameters(
            period
        ).gov.cra.tax.income.credits.gst_credit.childless_boost
        childless_phase_in = p.childless_phase_in.calc(net_income)
        childless_amount = min_(p.cap, childless_phase_in)
        amount_if_single = where(
            single_parent_household, p.cap, childless_amount
        )
        eligible = ~household("is_married", period)
        return eligible * amount_if_single
