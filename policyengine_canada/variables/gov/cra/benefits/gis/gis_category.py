from policyengine_canada.model_api import *

# Categories as listed in SPSD/M variable 'imoldtyp'
class GISCategory(Enum):
    NONE            = "none"
    SINGLE_WITH_OAS = "single_with_oas"
    WIDOW_60_64     = "widow_60_64"
    COUPLE_BOTH_OAS = "couple_both_oas"
    COUPLE_ELDER_OAS_YOUNGER_60_64 = "couple_elder_oas_younger_60_64"
    COUPLE_YOUNGER_OAS = "couple_younger_oas"

class gis_credit_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = GISCategory
    default_value = GISCategory.NONE
    definition_period = YEAR

    def formula(person, period, parameters):
        return select(
            [
                ~person("is_married", period) & person("old_age_security_pension_pre_repayment") > 0,
                person("is_widow", period) & person("age") < 65 & person("age") >= 60
             #   household("is_married", period) & add(household, period, ["is_spouse"] & ["old_age_security_pension_eligibility"]) > 0
            ],
            [
                GISCategory.SINGLE_WITH_OAS,
                GISCategory.WIDOW_60_64,
                GISCategory.COUPLE_BOTH_OAS
            ],
            default=0,
        )
