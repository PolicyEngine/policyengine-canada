from policyengine_canada.model_api import *


class canada_workers_benefit_dependent(Variable):
    value_type = bool
    entity = Person
    label = "Canada workers benefit dependent"
    definition_period = YEAR
