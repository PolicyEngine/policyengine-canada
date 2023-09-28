from policyengine_canada.model_api import *


class sk_infirm_dependant_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan Infirm Dependant Amount"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-lp-22e.pdf#page=6",
        "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=13 #page=14,15",
    )
    defined_for = "sk_infirm_dependant_amount_eligible_person"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.sk_infirm_dependant_amount
        eligible_person = person(
            "sk_infirm_dependant_amount_eligible_person", period
        )

        dependant_income = person("dependant_income", period)
        income_differences = max_(
            0, p.income_threshold.higher - dependant_income
        )

        return min_(p.amount, income_differences)
