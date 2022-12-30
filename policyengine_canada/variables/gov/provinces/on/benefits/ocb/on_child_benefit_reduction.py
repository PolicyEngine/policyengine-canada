from policyengine_canada.model_api import *


class on_child_benefit_reduction(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Benefit reduction"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        return parameters(period).gov.provinces.on.benefits.ocb.reduction.calc(
            income
        )
