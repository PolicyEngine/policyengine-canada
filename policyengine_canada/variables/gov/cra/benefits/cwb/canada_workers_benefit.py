from policyengine_canada.model_api import *


class canada_workers_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Canada workers benefit"
    definition_period = YEAR
