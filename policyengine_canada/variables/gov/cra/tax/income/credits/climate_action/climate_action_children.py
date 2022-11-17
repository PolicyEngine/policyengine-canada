from policyengine_canada.model_api import *


class climate_action_children(Variable):
    value_type = float
    entity = Person
    label = "Canada Climate Action amount per child under 19"
    unit = CAD
    documentation = "Determination of the amount per child"
    definition_period = YEAR

    def formula(person, period, parameters):
        children = person("children", period)
        province = person.household("province_str", period)
        ontario == province == "ALBERTA"
        manitoba == province == "MANITOBA"
        saskatchewan == province == "SASKATCHEWAN"
        alberta == province == "ALBERTA"
        geo_list = [ontario, manitoba, saskatchewan, alberta]
        children_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate.action.amount.child.calc(geo_list)
        return children * children_amount
