from policyengine_canada.model_api import *


class cwb_base_max_amount(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit max base amount"
    definition_period = YEAR

    def formula(household, period, parameters):
        p = parameters(period).gov.cra.benefits.cwb.amount
        family = household("is_cwb_family", period)
        eligible = household("cwb_eligible", period)
        return eligible * where(family, p.family, p.single)
