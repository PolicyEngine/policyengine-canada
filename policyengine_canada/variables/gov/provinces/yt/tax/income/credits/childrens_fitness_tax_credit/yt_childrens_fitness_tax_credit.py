from policyengine_canada.model_api import *


class yt_childrens_fitness_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Yukon children fitness tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        children = household("yt_cftc_eligible_children", period)
        disabled_children = household("yt_cftc_disabled_children", period)
