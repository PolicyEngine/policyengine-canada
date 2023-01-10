from policyengine_canada.model_api import *


class cwb_base_max_amount(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit max base amount"
    definition_period = YEAR
    defined_for = "cwb_eligible"

    def formula(household, period, parameters):
        p = parameters(period).gov.cra.benefits.cwb.amount
        family = household("is_cwb_family", period)
        return where(family, p.family, p.single)
