from policyengine_canada.model_api import *


class OEPTCSeniorStatus(Enum):
    SENIOR = "Has at least one senior"
    NON_SENIOR = "Has no seniors"


class oeptc_senior_status(Variable):
    value_type = Enum
    entity = Household
    label = "Is a senior for the OEPTC"
    possible_values = OEPTCSeniorStatus
    default_value = OEPTCSeniorStatus.NON_SENIOR
    definition_period = YEAR

    def formula(household, period, parameters):
        # TODO: Check this works.
        oldest_age = household.members("age", period).max(axis=0)
        p = parameters(period).gov.provinces.on.tax.income.credits.oeptc
        return where(
            oldest_age >= p.senior_age,
            OEPTCSeniorStatus.SENIOR,
            OEPTCSeniorStatus.NON_SENIOR,
        )
