from policyengine_canada.model_api import *


class OEPTCCategory(Enum):
    MARRIED = "Married"
    SINGLE_NO_CHILDREN = "Single with no children"
    SINGLE_SHARED_CUSTODY = "Single with shared custody of children"
    SINGLE_SOLE_CUSTODY = "Senior with sole custody of children"


class oeptc_category(Variable):
    value_type = Enum
    entity = Household
    possible_values = OEPTCCategory
    default_value = OEPTCCategory.SINGLE_SHARED_CUSTODY
    definition_period = YEAR

    def formula(household, period, parameters):
        married = household("is_married", period)
        children = household("oeptc_count_children", period)
        has_any_full_custody_children = (
            add(household, period, ["full_custody"]) > 0
        )
        return select(
            [married, children == 0, has_any_full_custody_children],
            [
                OEPTCCategory.MARRIED,
                OEPTCCategory.SINGLE_NO_CHILDREN,
                OEPTCCategory.SINGLE_SOLE_CUSTODY,
            ],
            default=OEPTCCategory.SINGLE_SHARED_CUSTODY,
        )
