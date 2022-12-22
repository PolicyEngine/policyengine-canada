from policyengine_canada.model_api import *


class CanadaWorkersBenefitDisabilityCategory(Enum):
    INELIGIBLE = "Ineligible"
    SINGLE = "Single"
    FAMILY_WITH_ONE_DISABLED_SPOUSE = "Family with one disabled spouse"
    FAMILY_WITH_TWO_DISABLED_SPOUSES = "Family with two disabled spouses"


class cwb_disability_category(Variable):
    value_type = Enum
    entity = Household
    possible_values = CanadaWorkersBenefitDisabilityCategory
    default_value = CanadaWorkersBenefitDisabilityCategory.INELIGIBLE
    label = "Canada workers benefit disability category"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        # Compute individual-level eligibility among heads/spouses.
        head_or_spouse = person("is_head_or_spouse", period)
        disability_eligible = person(
            "cwb_disability_supplement_eligible", period
        )
        cwb_family = household("is_cwb_family", period)
        eligible_spouses = household.sum(head_or_spouse * disability_eligible)
        return select(
            [
                eligible_spouses == 2,
                cwb_family & (eligible_spouses == 1),
                eligible_spouses == 1,
            ],
            [
                CanadaWorkersBenefitDisabilityCategory.FAMILY_WITH_TWO_DISABLED_SPOUSES,
                CanadaWorkersBenefitDisabilityCategory.FAMILY_WITH_ONE_DISABLED_SPOUSE,
                CanadaWorkersBenefitDisabilityCategory.SINGLE,
            ],
            default=CanadaWorkersBenefitDisabilityCategory.INELIGIBLE,
        )
