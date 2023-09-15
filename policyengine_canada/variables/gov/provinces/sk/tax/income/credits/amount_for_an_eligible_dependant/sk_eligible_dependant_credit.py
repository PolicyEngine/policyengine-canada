from policyengine_canada.model_api import *


class sk_eligible_dependant_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan eligible dependant credit"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=13",  # page=16
    )
    defined_for = "sk_eligible_dependant_credit_eligibility"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.amount_for_an_eligible_dependant
        dependant_income = person("dependant_income", period)
        reduction_threshold = dependant_income <= p.reduction.income_threshold
        reduced_amount = max_(p.reduction.base_amount - dependant_income, 0)

        return where(reduction_threshold, p.max_amount, reduced_amount)
