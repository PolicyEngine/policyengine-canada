from policyengine_canada.model_api import *


class head_income(Variable):
    value_type = float
    entity = Person
    label = "Head income"
    definition_period = YEAR

    def formula(person, period, parameters):
        head = person("is_head", period)
        income = person("individual_net_income", period)
        return head * income
