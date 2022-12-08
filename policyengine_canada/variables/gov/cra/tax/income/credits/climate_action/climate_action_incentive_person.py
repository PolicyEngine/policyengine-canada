from policyengine_canada.model_api import *


class climate_action_incentive_person(Variable):
    value_type = float
    entity = Person
    label = "Canada Climate Action amount per individual"
    unit = CAD
    documentation = "Determination of the amount per individual"
    definition_period = YEAR

    def formula(person, period, parameters):
        province = person.household("province_str", period)
        category = person("climate_action_incentive_category", period)
        amounts = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.amount
        return amounts[category][province]
