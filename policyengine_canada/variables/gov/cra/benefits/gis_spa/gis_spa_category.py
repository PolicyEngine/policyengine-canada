from policyengine_canada.model_api import *


# Categories as listed in SPSD/M variable 'imoldtyp'
class GISSPACategory(Enum):
    NONE = "none"
    SINGLE_WITH_OAS = "single_with_oas"
    WIDOW_SPA_ELIGIBLE = "widow_spa_eligible"
    COUPLE_BOTH_OAS = "couple_both_oas"
    COUPLE_ONE_OAS_SPA_ELIGIBLE = "couple_one_oas_spa_eligible"
    COUPLE_ONE_OAS_SPA_INELIGIBLE = "couple_one_oas_spa_ineligible"


class gis_spa_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = GISSPACategory
    default_value = GISSPACategory.NONE
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        age = person("age", period)
        age_spouse = household("age_spouse", period)
        married = household("is_married", period)
        widow = person("is_widow", period)
        oas_eligible = person("oas_eligible", period)
        spa_eligible = person("spa_eligible", period)
        spouse_oas_eligible = person("spouse_oas_eligible", period)
        spouse_spa_eligible = person("spouse_spa_eligible", period)
        return select(
            [
                ~married & oas_eligible,
                # The law specifies widows aged 60-64, but that cutoff of 64 is just because at 65 you become eligible for OAS. I just reference OAS eligibilty directly.
                widow & ~married & ~oas_eligible & spa_eligible,
                married & oas_eligible & spouse_oas_eligible,
                married
                & (
                    (oas_eligible & ~spouse_oas_eligible & spouse_spa_eligible)
                    | (~oas_eligible & spouse_oas_eligible & spa_eligible)
                ),
                married
                & (
                    (
                        oas_eligible
                        & ~spouse_oas_eligible
                        & ~spouse_spa_eligible
                    )
                    | (~oas_eligible & spouse_oas_eligible & ~spa_eligible)
                ),
            ],
            [
                GISSPACategory.SINGLE_WITH_OAS,
                GISSPACategory.WIDOW_SPA_ELIGIBLE,
                GISSPACategory.COUPLE_BOTH_OAS,
                GISSPACategory.COUPLE_ONE_OAS_SPA_ELIGIBLE,
                GISSPACategory.COUPLE_ONE_OAS_SPA_INELIGIBLE,
            ],
        )
