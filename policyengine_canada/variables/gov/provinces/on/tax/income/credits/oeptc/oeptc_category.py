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
        children = household("count_children", period)
        full_custody = household("full_custody", period)
        return select(
            [married, children == 0, full_custody],
            [
                OEPTCCategory.MARRIED,
                OEPTCCategory.SINGLE_NO_CHILDREN,
                OEPTCCategory.SINGLE_SOLE_CUSTODY,
            ],
            default=OEPTCCategory.SINGLE_SHARED_CUSTODY,
        )
