from policyengine_canada.model_api import *


class sk_spouse_or_common_law_partner_credit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan spouse or common law partner credit"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=12",
    )
    defined_for = "sk_spouse_or_common_law_partner_credit_eligible"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.spouse_or_common_law_partner_amount
        person = household.members
        spouse_income = household.sum(person("spouse_income", period))
        reduction_threshold = spouse_income <= p.reduction.income_threshold
        reduced_amount = max_(p.reduction.base_amount - spouse_income, 0)

        return where(reduction_threshold, p.max_amount, reduced_amount)
