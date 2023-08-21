
from policyengine_canada.model_api import *


class sk_spouse_or_common_law_partner_credit_eligible(Variable):
    value_type = float
    entity = Household
    label = "Eligible for the Saskatchewan spouse or common law partner credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        live_with_spouse = household("cohabitating_spouses", period)
        person = household.members
        head = person("is_head", period)

        return household.any(head) * live_with_spouse