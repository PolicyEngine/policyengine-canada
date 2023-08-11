from policyengine_canada.model_api import *


class sk_pension_income_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan pension income credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=16",
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.pension_income_amount
        # Payments exclude Canada Pension Plan, Quebec Pension Plan, Old Age Security, or Guaranteed Income Supplement payments
        pension_payments = person("pension_and_savings_plan_income", period)
        max_amount = p.maximum_amount
        return min_(pension_payments, max_amount)
