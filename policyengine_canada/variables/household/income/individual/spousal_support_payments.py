from policyengine_canada.model_api import *


class spousal_support_payments(Variable):
    value_type = float
    entity = Person
    label = "Spousal support payments"
    unit = CAD
    documentation = "Money paid by one spouse to the other after they separate or divorce"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/p102/support-payments.html"
