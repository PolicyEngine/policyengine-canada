from policyengine_canada.model_api import *


class nl_child_benefit_supplement(Variable):
    value_type = float
    entity = Household
    label = "Newfoundland and Labrador child benefit supplement"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(household, period, parameters):
        person = household.members 
        children = household("nl_child_benefit_supplement_children", period)
        p = parameters(
            period
        ).gov.provinces.nl.benefits.child_benefits.supplement
        pregant = person("is_pregnant", period)
        # the supplement amount would be zero if no child under age 1.
        # the supplement amount would be base amount if any child under age 1. 
        eligible = (children >= 1) | household.any(pregant)
        return where(eligible, p.base, 0)

