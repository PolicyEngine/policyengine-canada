from policyengine_canada.model_api import *


class sk_caregiver_amount_eligibile_person(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan Caregiver Amount Eligibility"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-lp-22e.pdf#page=5",
        "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=13,14,16,17",
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.sk_caregiver_amount

        age = person("age", period)
        dependant = person("is_live_together_dependant", period)
        disabled = person("is_disabled", period)
        parent_or_grandparent = person("parent_or_grandparent", period)

        is_infirm_dependant = dependant & disabled
        is_elderly_dependant = dependant & parent_or_grandparent

        infirm_age_eligibility = age >= p.age_threshold.infirm
        elderly_age_eligibility = age >= p.age_threshold.elderly

        infirm_eligibility = is_infirm_dependant & infirm_age_eligibility
        elderly_eligibility = is_elderly_dependant & elderly_age_eligibility

        dependants_income = person("individual_net_income", period)
        income_eligibility = dependants_income <= p.higher_income_threshold

        return income_eligibility & (infirm_eligibility | elderly_eligibility)
