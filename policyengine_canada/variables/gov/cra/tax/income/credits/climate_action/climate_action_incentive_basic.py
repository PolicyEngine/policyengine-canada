from policyengine_canada.model_api import *


class climate_action_incentive_basic(Variable):
    value_type = float
    entity = Household
    label = "Canada Climate Action amount per individual"
    unit = CAD
    documentation = "Determination of the amount per individual"
    definition_period = YEAR

    def formula(household, period, parameters):
        province = household("province_str", period)
        return parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.amount.basic[
            province
        ]
