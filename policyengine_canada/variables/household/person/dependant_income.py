from policyengine_canada.model_api import *


class dependant_income(Variable):
    value_type = float
    entity = Person
    label = "Dependant's net income"
    definition_period = YEAR

    def formula(person, period, parameters):
        dependant = person("is_dependant", period)
        income = person("individual_net_income", period)
        return dependant * income
