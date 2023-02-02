from policyengine_canada.model_api import *


# SPSD/M 29.0: imioas or imoasmax, I'm not sure. I think imioas is post-repayment?
class oas_net(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension pre-repayment"
    documentation = "The OAS amount a person is eligible for prior to the repayment tax. See SPSD/M 'imoasmax'."
    unit = CAD
    definition_period = YEAR
    adds = ["oas_pre_repayment"]
    subtracts = ["oas_repayment"]
