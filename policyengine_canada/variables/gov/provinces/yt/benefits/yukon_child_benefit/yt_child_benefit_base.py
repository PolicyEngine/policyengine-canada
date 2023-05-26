from policyengine_canada.model_api import *


class yt_child_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "Yukon child benefit base"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        children = household("yt_child_benefit_eligible_children", period)
        return (
            children
            * parameters(period).gov.provinces.yt.benefits.child_benefit.base
        )
