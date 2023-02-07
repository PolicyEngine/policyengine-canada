from policyengine_canada.model_api import *


class is_eldest_child_for_bc_climate_action_tax_credit(Variable):
    value_type = bool
    entity = Person
    label = "Is the first born child in a household, for the purposes of the British Columbia climate action tax credit "
    definition_period = YEAR
    defined_for = "is_child_for_bc_climate_action_tax_credit"

    def formula(person, period, parameters):
        household = person.household
        ix = person("person_index", period)
        child = person("is_child_for_bc_climate_action_tax_credit", period)
        child_index = where(child, ix, 100)
        household_min_child_index = household.min(child_index)
        has_min_child_index = household_min_child_index == ix
        return has_min_child_index & child
