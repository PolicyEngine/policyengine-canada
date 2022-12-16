from policyengine_canada.model_api import *


class canada_workers_benefit_category(Variable):
    value_type = bool
    entity = Household
    label = "Canada workers benefit category"
    definition_period = YEAR
