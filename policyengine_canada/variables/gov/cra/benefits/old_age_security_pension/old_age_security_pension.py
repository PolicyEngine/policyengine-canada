from policyengine_canada.model_api import *

# SPSD/M 29.0: imioas or imoasmax, I'm not sure. I think imioas is post-repayment?
class old_age_security_pension(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension pre-repayment"
    documentation = "The OAS amount a person is eligible for prior to the repayment tax. See SPSD/M 'imoasmax'."
    unit = CAD
    definition_period = YEAR
    adds = ["old_age_security_pension_pre_repayment"]
    subtracts = ["old_age_security_pension_repayment"]
