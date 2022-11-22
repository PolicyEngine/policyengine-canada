from policyengine_canada.model_api import *


class climate_action_incentive_dependent_children(Variable):
    value_type = int
    entity = Household
    label = "Climate action incentive dependent Children"
    unit = CAD
    documentation = "Number of eligible dependent children"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        dependent = person("is_dependent", period)
        age = person("age", period)
        adult_age = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.adult_age
        is_child_dependent = dependent & (age < adult_age)
        return household.sum(is_child_dependent)


# The definition of an eligible child also includes living with parents and eligibilty under CCB
