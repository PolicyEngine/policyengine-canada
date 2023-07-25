from policyengine_canada.model_api import *


class sk_transferred_from_spouse_or_common_law_partner_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan transferred from spouse or common-law partner credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download",
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):

        age_amount = person("sk_age_amount", period)
        senior_supplementary_amount = person(
            "sk_senior_supplementary_credit", period
        )
        pension_income_amount = person("sk_pension_income_credit", period)
        disability_amount = person("sk_disability_amount", period)
        child_amount = person("sk_child_amount", period)
        spouse = person("is_spouse", period)

        spouse_used_age_amount = age_amount * (spouse == True)
        spouse_used_senior_supplementary_amount = (
            senior_supplementary_amount * (spouse == True)
        )
        spouse_used_pension_income_amount = pension_income_amount * (
            spouse == True
        )
        spouse_used_disability_amount = disability_amount * (spouse == True)
        spouse_used_child_amount = child_amount * (spouse == True)
        total = (
            age_amount
            + senior_supplementary_amount
            + pension_income_amount
            + disability_amount
            + child_amount
        )

        spouse_used_amount = (
            spouse_used_age_amount
            + spouse_used_senior_supplementary_amount
            + spouse_used_pension_income_amount
            + spouse_used_disability_amount
            + spouse_used_child_amount
        )

        return total - spouse_used_amount
