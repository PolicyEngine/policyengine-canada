from policyengine_canada.model_api import *


class spouse_or_common_law_partner_amount_eligible_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Eligible spouse for the spouse or common law partner amount"
    definition_period = YEAR


# TODO: formula
