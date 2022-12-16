from policyengine_canada.model_api import *


class canada_workers_benefit_disability_supplement(Variable):
    value_type = bool
    entity = Household
    label = "Canada workers benefit disability supplement"
    definition_period = YEAR
