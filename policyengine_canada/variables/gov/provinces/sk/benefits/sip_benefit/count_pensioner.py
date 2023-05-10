from policyengine_canada.model_api import *


class count_pensioner(Variable):
    value_type = int
    entity = Household
    label = "Pensioner"
    documentation = "Number of pensioners in household"
    definition_period = YEAR