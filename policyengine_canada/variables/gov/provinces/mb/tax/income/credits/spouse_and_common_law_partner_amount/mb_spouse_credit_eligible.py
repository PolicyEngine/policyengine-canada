from policyengine_canada.model_api import *


class mb_spouse_credit_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Manitoba head eligiblility for recieving spouse's tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(household, period, parameters):
        return household("cohabitating_spouses", period)
