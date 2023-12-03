from policyengine_canada.model_api import *


class infirm_dependant_income(Variable):
    value_type = float
    entity = Person
    label = "Infirm dependant income"
    definition_period = YEAR

    def formula(person, period, parameters):
        infirm_dependant = person("is_infirm_dependant", period)
        income = person("individual_net_income", period)
        return infirm_dependant * income
