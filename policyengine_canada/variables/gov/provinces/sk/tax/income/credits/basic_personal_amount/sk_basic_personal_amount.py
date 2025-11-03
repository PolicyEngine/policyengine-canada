from policyengine_canada.model_api import *


class sk_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan basic personal amount"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download",
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.basic_personal_amount

        return p.basic_personal_amount
