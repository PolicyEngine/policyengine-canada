from policyengine_canada.model_api import *


class yt_child_benefit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon child benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        return person("is_dependent", period)
