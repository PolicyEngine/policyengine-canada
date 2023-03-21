from policyengine_canada.model_api import *


class yt_childrens_arts_credit_expenses(Variable):
    value_type = float
    entity = Household
    label = "Yukon childrens arts credit expenses"
    definition_period = YEAR
    defined_for = ProvinceCode.YT
