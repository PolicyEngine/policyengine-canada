from policyengine_canada.model_api import *


class is_mother(Variable):
    value_type = bool
    entity = Person
    label = "Is a mother"
    definition_period = YEAR

    def formula(person, period, parameters):
        female = person("is_female", period)
        has_children = person("own_children_in_household", period) > 0
        # breastfeeding = person("is_breastfeeding", period)
        # return breastfeeding | (female & has_children)
        return female & has_children
