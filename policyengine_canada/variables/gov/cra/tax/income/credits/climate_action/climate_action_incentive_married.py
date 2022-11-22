from policyengine_canada.model_api import *


class climate_action_incentive_married(Variable):
    value_type = float
    entity = Household
    label = (
        "Canada Climate Action amount for the spouse in a married household"
    )
    unit = CAD
    documentation = (
        "Determination of the amount for the spouse in a married household"
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        spouse = household("is_married", period)
        province = household("province_str", period)
        spouse_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.amount.spouse[
            province
        ]
        return spouse * spouse_amount
