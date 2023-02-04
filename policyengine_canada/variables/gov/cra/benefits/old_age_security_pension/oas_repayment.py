from policyengine_canada.model_api import *


class oas_repayment(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension repayment"
    documentation = "Your repayment calculation is based on the difference between your income and the threshold amount for the year. The first step is to figure out how much higher your income is than the threshold. You must repay 15 percent of that amount. See OASTD and OASRR in the SPSD/M Parameter Guide"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.old_age_security_pension
        # The income concept in the documentation is 'net world income'. I just use net income here.
        net_income = person("individual_net_income", period)
        # The repayment tax is a percent of income above a threshold.
        uncapped_repayment_tax = p.repayment_tax.calc(net_income)
        # Cap repayment at the pre-repayment amount.
        oas_pre_repayment = person("oas_pre_repayment", period)
        repayment_tax = min_(oas_pre_repayment, uncapped_repayment_tax)

        # Round to the nearest cent.
        return numpy.around(repayment_tax, 2)
