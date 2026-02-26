from policyengine_canada.model_api import *


class is_single(Variable):
    value_type = bool
    entity = Household
    label = "Is single household"
    definition_period = YEAR
    documentation = "Whether the household has only one adult (no spouse/partner)"

    def formula(household, period, parameters):
        # Count the number of heads and spouses in the household
        num_heads = household.sum(household.members("is_head", period))
        num_spouses = household.sum(household.members("is_spouse", period))
        
        # A single household has a head but no spouse
        return (num_heads == 1) & (num_spouses == 0)