from policyengine_canada.model_api import *


class bc_tuition_credit_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the British Columbia tuition credit"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-32300-your-tuition-education-textbook-amounts/eligible-tuition-fees.html",  # Tuition Amount
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nb/td1nb-23e.pdf#page=1",
        "https://laws-lois.justice.gc.ca/PDF/I-3.3.pdf#page=1566",  # Line 4
    )
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.tuition_amount
        age = person("age", period)
        tuition = person("tuition_expenses", period)
        return (age >= p.eligible_age) & (tuition >= p.tuition_threshold)
