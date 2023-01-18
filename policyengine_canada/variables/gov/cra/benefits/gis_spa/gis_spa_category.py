from policyengine_canada.model_api import *

# Categories as listed in SPSD/M variable 'imoldtyp'
class GISSPACategory(Enum):
    NONE            = "none"
    SINGLE_WITH_OAS = "single_with_oas"
    WIDOW_60_64     = "widow_60_64"
    COUPLE_BOTH_OAS = "couple_both_oas"
    COUPLE_ELDER_OAS_YOUNGER_60_64 = "couple_elder_oas_younger_60_64"
    COUPLE_YOUNGER_OAS = "couple_younger_oas"
    COUPLE_ELDER_OAS = "couple_elder_oas"

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
        head = person("is_head", period)
        spouse = person("is_spouse", period)
        widow = person("is_widow", period)
        oas_eligible = person("old_age_security_pension_eligibility", period)
        spouse_oas_eligible = person("spouse_oas_eligible", period)
        p = parameters(period).gov.cra.benefits.gis_spa
        return select(
            [
                ~married & oas_eligible,
                # The law specifies widows aged 60-64, but that cutoff of 64 is just because at 65 you become eligible for OAS. I just reference OAS eligibilty directly.
                widow & ~married & ~oas_eligible & (age >= p.spa_widows_eligibility_age),
                married & oas_eligible & spouse_oas_eligible, 
                married & (head & oas_eligible & ~spouse_oas_eligible & (age_spouse >= p.spa_eligibility_age)) | (spouse & ~oas_eligible & spouse_oas_eligible & (age >= p.spa_eligibility_age)),
               # married & (head & oas_eligible & ~spouse_oas_eligible & (age_spouse >= p.spa_eligibility_age))
            ],
            [
                GISSPACategory.SINGLE_WITH_OAS,
                GISSPACategory.WIDOW_60_64,
                GISSPACategory.COUPLE_BOTH_OAS,
                GISSPACategory.COUPLE_ELDER_OAS_YOUNGER_60_64,
               # GISSPACategory.COUPLE_YOUNGER_OAS,
                
            ],
            default=0,
        )
