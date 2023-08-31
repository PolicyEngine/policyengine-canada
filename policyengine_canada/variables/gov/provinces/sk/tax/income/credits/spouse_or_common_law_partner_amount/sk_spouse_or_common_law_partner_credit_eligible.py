from policyengine_canada.model_api import *


class sk_spouse_or_common_law_partner_credit_eligible(Variable):
    value_type = float
    entity = Household
    label = "Eligible for the Saskatchewan spouse or common law partner credit"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=12",
    )
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        return household("cohabitating_spouses", period)
