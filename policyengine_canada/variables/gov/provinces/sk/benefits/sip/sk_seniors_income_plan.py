from policyengine_canada.model_api import *


class sk_seniors_income_plan(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan seniors income plan"
    definition_period = YEAR
    defined_for = ProvinceCode.SK


    adds = ["sk_seniors_income_plan_at_home", "sk_seniors_income_plan_in_special_care_home"]