from policyengine_canada.model_api import *


class dental_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada dental benefit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        full_custody_amount = household("dental_benefit_full_custody", period)
        shared_custody_amount = household(
            "dental_benefit_shared_custody", period
        )
        return full_custody_amount + shared_custody_amount


# TODO additional benefit (if dental expenses exceed 650 CAD)
