from policyengine_canada.model_api import *


class on_senior_homeowners_property_tax_grant(Variable):
    value_type = float
    entity = Person
    label = "Ontario senior homeowners property tax grant"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        base = household(
            "on_senior_homeowners_property_tax_grant_base", period
        )
        reduction = household(
            "on_senior_homeowners_property_tax_grant_reduction", period
        )
        return max_(0, base - reduction)
