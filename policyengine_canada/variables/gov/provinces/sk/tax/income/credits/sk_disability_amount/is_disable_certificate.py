from policyengine_canada.model_api import *


class is_disable_certificate(Variable):
    value_type = bool
    entity = Person
    label = "have disability tax credit certificate"
    definition_period = YEAR
    defined_for = ProvinceCode.SK
