from policyengine_canada.model_api import *


class sk_age_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan age amount credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-21e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1-ws/td1-ws-21e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1-ws/td1-ws-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1-ws/td1-ws-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=15",
    )
    defined_for = "sk_age_amount_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.age_amount
        income = person("individual_net_income", period)
        reduction = p.reduction.rate.calc(income)
        return max_(p.max_amount - reduction, 0)
