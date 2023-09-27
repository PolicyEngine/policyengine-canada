from policyengine_canada.model_api import *


class nb_tuition_eligible(Variable):
    value_type = bool
    entity = Person
    label = "New Brunswick tuiton eligibility"
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nb/td1nb-23e.pdf#page=1"
    defined_for = "nb_age_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.tuition_amount
        tuition = person("tuition_expenses", period)
        return tuition >= p.tuition_threshold
