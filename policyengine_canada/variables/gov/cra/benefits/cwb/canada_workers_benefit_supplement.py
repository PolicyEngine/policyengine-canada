from policyengine_canada.model_api import *


class canada_workers_benefit_supplement(Variable):
    value_type = bool
    entity = Person
    label = "Canada workers benefit supplement amount"
    definition_period = YEAR
