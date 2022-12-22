from policyengine_canada.model_api import *


class cwb_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Canada workers benefit dependant"
    definition_period = YEAR
    reference = ""  # TODO: Add

    def formula(person, period, parameters):
        return ~person("cwb_eligible", period)
