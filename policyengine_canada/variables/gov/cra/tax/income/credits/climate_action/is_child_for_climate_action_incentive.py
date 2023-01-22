from policyengine_canada.model_api import *


class is_child_for_climate_action_incentive(Variable):
    value_type = bool
    entity = Person
    label = "Is the first born child in a Household"
    definition_period = YEAR

    def formula(person, period, parameters):
        dependent = person("is_dependent", period)
        age = person("age", period)
        adult_age = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.adult_age
        return dependent & (age < adult_age)
        # The definition of an eligible child also includes living with
        # parents and eligibilty under CCB. These are not included here.
