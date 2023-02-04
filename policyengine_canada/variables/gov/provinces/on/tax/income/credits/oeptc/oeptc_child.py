from policyengine_canada.model_api import *


class oeptc_child(Variable):
    value_type = bool
    entity = Person
    label = "Is a child for the Ontario Energy and Property Tax Credit"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.oeptc
        return age < p.child_max_age
