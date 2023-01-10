from policyengine_canada.model_api import *


class OEPTCCategory(Enum):
    SENIOR_MARRIED = "Senior married"
    SENIOR_SINGLE_NO_CHILDREN = "Senior married"
    SENIOR_SINGLE_SHARED_CUSTODY = "Senior married"
    SENIOR_SINGLE_SOLE_CUSTODY = "Senior married"
    NON_SENIOR_MARRIED = "Non-senior, married"
    NON_SENIOR_SINGLE_NO_CHILDREN = "Non-senior, single without children"
    NON_SENIOR_SINGLE_SHARED_CUSTODY = (
        "Non-senior, single with shared custody children"
    )
    NON_SENIOR_SINGLE_SOLE_CUSTODY = (
        "Non-senior, single with sole custody children"
    )


class oeptc_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = OEPTCCategory
    default_value = OEPTCCategory.NON_SENIOR_SINGLE_NO_CHILDREN
    definition_period = YEAR

    def formula(person, period, parameters):
        senior = person("is_senior_for_oeptc", period)
        married = person("is_married", period)
        children = person("count_cchildren", period)
        full_custody = person("full_custody", period)
        return select(
            [
                senior & married,
                senior & ~married & children == 0,
                senior & ~married & children > 0 & ~full_custody,
                senior & ~married & children > 0 & full_custody,
                ~senior & married,
                ~senior & ~married & children == 0,
                ~senior & ~married & children > 0 & ~full_custody,
                ~senior & ~married & children > 0 & full_custody,
            ],
            [
                OEPTCCategory.SENIOR_MARRIED,
                OEPTCCategory.SENIOR_SINGLE_NO_CHILDREN,
                OEPTCCategory.SENIOR_SINGLE_SHARED_CUSTODY,
                OEPTCCategory.SENIOR_SINGLE_SOLE_CUSTODY,
                OEPTCCategory.NON_SENIOR_MARRIED,
                OEPTCCategory.NON_SENIOR_SINGLE_NO_CHILDREN,
                OEPTCCategory.NON_SENIOR_SINGLE_SHARED_CUSTODY,
                OEPTCCategory.NON_SENIOR_SINGLE_SOLE_CUSTODY,
            ],
        )
