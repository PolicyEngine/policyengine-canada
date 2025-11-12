from policyengine_canada.model_api import *


class sk_pension_income_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan pension income credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download",
    )
    defined_for = ProvinceCode.SK
