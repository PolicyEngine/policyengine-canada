from policyengine_canada.model_api import *


class spouse_income(Variable):
    value_type = float
    entity = Person
    label = "Spouse and commonlaw partner income"
    definition_period = YEAR

    def formula(person, period, parameters):
        spouse = person("is_spouse", period)
        income = person("individual_net_income", period)
        return spouse * income
