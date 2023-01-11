from policyengine_canada.model_api import *


class is_eldest_child_in_single_household_for_gst_credit(Variable):
    value_type = bool
    entity = Person
    label = "Is this person the first born child in a single-parent household?"
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        ix = person("person_index", period)
        child = person("is_child_for_gst_credit", period)
        child_index = where(child, ix, 100)
        household_min_child_index = household.min(child_index)
        has_min_child_index = household_min_child_index == ix
        return has_min_child_index & child & ~household("is_married", period)
