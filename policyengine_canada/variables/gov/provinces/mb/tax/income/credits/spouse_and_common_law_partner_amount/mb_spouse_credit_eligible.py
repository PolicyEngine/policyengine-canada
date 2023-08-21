from policyengine_canada.model_api import *


class mb_spouse_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba head eligiblility for recieving spouse's tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        return person("is_caregiver", period)
