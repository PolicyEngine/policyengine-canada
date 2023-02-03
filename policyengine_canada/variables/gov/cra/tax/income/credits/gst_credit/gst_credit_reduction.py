from policyengine_canada.model_api import *


class gst_credit_reduction(Variable):
    value_type = float
    entity = Household
    label = "GST Credit reduction based on income"
    unit = CAD
    definition_period = YEAR

    # The income concept here is supposed to be based on a slightly modified version of family net income,
    # where you subtract certain income sources such as Registered Disability Savings Plan income. I've ignored
    # these modifications and just used net income.
    def formula(household, period, parameters):
        net_income = household("household_net_income", period)

        reduction = parameters(
            period
        ).gov.cra.tax.income.credits.gst_credit.reduction.calc(net_income)
        # Round to the nearest cent.
        return numpy.around(reduction, 2)
