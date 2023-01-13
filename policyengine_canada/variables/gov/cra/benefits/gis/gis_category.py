rom policyengine_canada.model_api import *


# Categories as listed in SPSD/M variable 'imoldtyp'
class GISCategory(Enum):
    SINGLE_WITH_OAS = "single_with_oas"
    WIDOW_60_64     = "widow_60_64"
    COUPLE_BOTH_OAS = "couple_both_oas"
    COUPLE_ELDER_OAS_YOUNGER_60_64 = "couple_elder_oas_younger_60_64"
    COUPLE_YOUNGER_OAS = "couple_younger_oas"

class gst_credit_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = GSTCreditCategory
    default_value = GSTCreditCategory.HEAD
    definition_period = YEAR

    def formula(person, period, parameters):
        return select(
            [
                ~person("is_married", period) & person("old_age_security_pension_pre_repayment") > 0
            ],
            [
                GISCategory.SINGLE_WITH_OAS
            ],
            default=0,
        )
