from policyengine_canada.model_api import *


class ei_insurable_hours(Variable):
    value_type = float
    entity = Person
    label = "Employment Insurance insurable hours"
    definition_period = YEAR
    unit = "hour"
    documentation = "Number of insurable hours worked in the qualifying period"