from policyengine_canada.model_api import *


class canada_workers_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit"
    definition_period = YEAR
    unit = CAD

    adds = ["cwb_base", "cwb_disability_supplement"]
