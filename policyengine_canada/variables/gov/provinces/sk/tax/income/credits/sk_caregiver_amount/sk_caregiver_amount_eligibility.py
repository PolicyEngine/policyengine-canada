from policyengine_canada.model_api import *


class sk_caregiver_amount_eligibility(Variable):
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

        infirm_age_eligibility = (
            person("age", period) >= p.age_threshold.infirm
        )
        elderly_age_eligibility = (
            person("age", period) >= p.age_threshold.elderly
        )

        infirm_eligibility = (
            person("is_infirm_dependant", period) & infirm_age_eligibility
        )
        elderly_eligibility = (
            person("is_elderly_dependant", period) & elderly_age_eligibility
        )

        dependants_income = person("individual_net_income", period)
        income_eligibility = dependants_income <= p.higher_income_threshold

        return income_eligibility & (infirm_eligibility | elderly_eligibility)
