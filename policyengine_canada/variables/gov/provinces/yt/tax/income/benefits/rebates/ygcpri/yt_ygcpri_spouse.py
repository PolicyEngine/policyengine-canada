from policyengine_canada.model_api import *


class yt_ygcpri_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Yukon ygcpri eligible spouse"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        return person("is_spouse", period)