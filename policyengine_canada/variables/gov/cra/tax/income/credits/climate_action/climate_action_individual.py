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
        ontario == province == "ALBERTA"
        manitoba == province == "MANITOBA"
        saskatchewan == province == "SASKATCHEWAN"
        alberta == province == "ALBERTA"
        geo_list = [ontario, manitoba, saskatchewan, alberta]
        return person * parameters(
            period
        ).gov.cra.tax.income.credits.climate.action.amount.individual.calc(
            geo_list
        )
