from policyengine_canada.model_api import *


class ClimateActionIncentiveCategory(Enum):
    HEAD = "Head"
    SPOUSE = "Spouse"
    ELDEST_CHILD_IN_SINGLE_PARENT_HOUSEHOLD = (
        "Eldest child in single parent household"
    )
    OTHER_CHILD = "Other child"


class climate_action_incentive_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = ClimateActionIncentiveCategory
    default_value = ClimateActionIncentiveCategory.HEAD
    definition_period = YEAR

    def formula(person, period, parameters):
        is_single_parent_household = person.household(
            "climate_action_incentive_single_parent_household", period
        )
        eldest_child = person(
            "is_eldest_child_for_climate_action_incentive", period
        )
        eldest_child_in_single_parent_household = (
            is_single_parent_household & eldest_child
        )
        other_child = (
            person("is_child_for_climate_action_incentive", period)
            & ~eldest_child_in_single_parent_household
        )
        return select(
            [
                person("is_head", period),
                person("is_spouse", period),
                eldest_child_in_single_parent_household,
                other_child,
            ],
            [
                ClimateActionIncentiveCategory.HEAD,
                ClimateActionIncentiveCategory.SPOUSE,
                ClimateActionIncentiveCategory.ELDEST_CHILD_IN_SINGLE_PARENT_HOUSEHOLD,
                ClimateActionIncentiveCategory.OTHER_CHILD,
            ],
        )
