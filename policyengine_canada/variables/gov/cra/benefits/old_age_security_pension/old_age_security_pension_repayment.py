from policyengine_canada.model_api import *

# SPSD/M 29.0: imioas or imoasmax, I'm not sure. I think imioas is post-repayment?


class old_age_security_pension_repayment(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension repayment"
    documentation = "Your repayment calculation is based on the difference between your income and the threshold amount for the year. The first step is to figure out how much higher your income is than the threshold. You must repay 15 percent of that amount. See OASTD and OASRR in the SPSD/M Parameter Guide"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.old_age_security_pension.amount
        # The income concept in the documentation is 'net world income'. I just use net income here.
        net_income = person("individual_net_income", period)
        oas_pre_repayment = person(
            "old_age_security_pension_pre_repayment", period
        )
        difference = max(net_income - p.repayment_threshold, 0)
        repayment = min(oas_pre_repayment, (difference * p.repayment_rate))

        # Round to the nearest cent.
        return numpy.around(repayment, 2)
