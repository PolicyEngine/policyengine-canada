from policyengine_canada.model_api import *


class nb_tuition_credit_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the New Brunswick tuition credit"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pub/p105/p105-22e.pdf#page=11",  # Tuition Amount
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nb/td1nb-23e.pdf#page=1",  # Line 4
    )
    defined_for = ProvinceCode.NB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.tuition_amount
        age = person("age", period)
        tuition = person("tuition_expenses", period)
        return (age >= p.eligible_age) & (tuition >= p.tuition_threshold)
