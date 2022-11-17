from policyengine_canada.model_api import *


class climate_action_head(Variable):
    value_type = float
    entity = Person
    label = "Canada Climate Action amount per child under 19"
    unit = CAD
    documentation = "Determination of the amount per child"
    definition_period = YEAR

    def formula(person, period, parameters):
        person = person("is_adult", period)
        province = person.household("province_str", period)
        children_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action.amount.child[province]
        return person * children_amount
