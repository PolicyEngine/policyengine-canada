from policyengine_canada.model_api import *


class sk_seniors_income_plan(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan seniors income plan"
    definition_period = YEAR
    defined_for = ProvinceCode.SK


    #adds = ["sk_seniors_income_plan_at_home", "sk_seniors_income_plan_in_special_care_home"]

    def formula(household, period, parameters):
        sip_at_home = household("sk_seniors_income_plan_at_home", period)
        sip_in_special_care_home = household("sk_seniors_income_plan_in_special_care_home", period)
        sip = sip_at_home + sip_in_special_care_home
        return household.sum(sip)