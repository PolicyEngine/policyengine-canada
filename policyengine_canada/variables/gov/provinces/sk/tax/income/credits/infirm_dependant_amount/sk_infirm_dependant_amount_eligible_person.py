from policyengine_canada.model_api import *


class sk_infirm_dependant_amount_eligible_person(Variable):
    value_type = bool
    entity = Person
    label = "Eligible person for the Saskatchewan Infirm Dependants Amount"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-lp-22e.pdf#page=6",
        "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=13 #page=14,15",
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.sk_infirm_dependant_amount

        age = person("age", period)
        dependant = person("is_child_of_filer", period)
        disabled = person("is_disabled", period)

        is_infirm_dependant = dependant & disabled
        infirm_age_eligibility = age >= p.age_threshold

        infirm_eligibility = is_infirm_dependant & infirm_age_eligibility

        dependants_income = person("dependant_income", period)
        income_eligibility = dependants_income <= p.income_threshold.higher

        infirm_dependant_amount_for_line9 = person("sk_caregiver_amount", period)
        duplicate_infirm_dependant = where(infirm_dependant_amount_for_line9 == 0, 0, 1)

        return infirm_eligibility & ~duplicate_infirm_dependant & income_eligibility