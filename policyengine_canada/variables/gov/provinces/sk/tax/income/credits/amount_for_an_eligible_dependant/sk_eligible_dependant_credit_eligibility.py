from policyengine_canada.model_api import *


class sk_eligible_dependant_credit_eligibility(Variable):
    value_type = bool
    entity = Person
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

    def formula(person, period, parameters):
        live_together = person.household("joint_living", period)
        dependant = person("is_dependant", period)
        is_related = person("is_relative", period)
        dependant_eligible = live_together & dependant & is_related
        spouse = person("is_spouse", period)
        support = person("is_supportive", period)
        cohabitating_spouses = person.household("cohabitating_spouses", period)
        head_eligible = (~spouse) | (~cohabitating_spouses & ~support)

        return dependant_eligible * head_eligible
