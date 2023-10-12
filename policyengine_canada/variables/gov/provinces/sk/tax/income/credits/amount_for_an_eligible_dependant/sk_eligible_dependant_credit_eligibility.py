from policyengine_canada.model_api import *


class sk_eligible_dependant_credit_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Eligibility for the Saskatchewan amount for an eligible dependant credit"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=13",  # page=16
    )
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        person = household.members
        live_together = person("cohabitating_dependant", period)
        dependant = person("is_dependant", period)
        is_related = person("is_related", period)
        dependant_eligible = live_together & dependant & is_related
        spouse = person("is_spouse", period)
        no_spouse_present = household.min(~spouse)
        spouse_is_supported = household("spouse_is_supported", period)
        cohabitating_spouses = household("cohabitating_spouses", period)
        # The household is eligible if there is no spouse present or if the spouse
        # does not live with the head and is not supported
        spouse_condition_eligible = no_spouse_present | ((~cohabitating_spouses) & (~spouse_is_supported))
        return household.any(dependant_eligible & spouse_condition_eligible)

# household.min should be applied to not spouse 
