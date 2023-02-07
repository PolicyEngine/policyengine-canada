from policyengine_canada.model_api import *


class BCClimateActionIncentiveCategory(Enum):
    HEAD = "Head"
    SPOUSE = "Spouse"
    ELDEST_CHILD_IN_SINGLE_PARENT_HOUSEHOLD = (
        "Eldest child in single parent household"
    )
    OTHER_CHILD = "Other child"


class bc_climate_action_incentive_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = BCClimateActionIncentiveCategory
    default_value = BCClimateActionIncentiveCategory.HEAD
    definition_period = YEAR

    def formula(person, period, parameters):
        is_single_parent_household = person.household(
            "bc_climate_action_tax_credit_single_parent_household", period
        )
        eldest_child = person(
            "is_eldest_child_for_bc_climate_action_tax_credit", period
        )
        eldest_child_in_single_parent_household = (
            is_single_parent_household & eldest_child
        )
        other_child = (
            person("is_child_for_bc_climate_action_tax_credit", period)
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
                BCClimateActionIncentiveCategory.HEAD,
                BCClimateActionIncentiveCategory.SPOUSE,
                BCClimateActionIncentiveCategory.ELDEST_CHILD_IN_SINGLE_PARENT_HOUSEHOLD,
                BCClimateActionIncentiveCategory.OTHER_CHILD,
            ],
        )
