from policyengine_canada.model_api import *


class climate_action_single_parent(Variable):
    value_type = float
    entity = Person
    label = "Canada Climate Action single parent amount"
    unit = CAD
    documentation = "Determination wether the filer is a single parent eligible for the climate action incentive"
    definition_period = YEAR

    def formula(person, period, parameters):
        single_parent = person("is_single_parent", period)
        province = person.household("province_str", period)
        children_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate.action.amount.child[province]
        return single_parent * children_amount
