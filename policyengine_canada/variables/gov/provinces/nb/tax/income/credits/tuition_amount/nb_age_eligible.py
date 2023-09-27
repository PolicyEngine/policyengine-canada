from policyengine_canada.model_api import *


class nb_age_eligible(Variable):
    value_type = bool
    entity = Person
    label = "New Brunswick age eligibility"
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pub/p105/p105-22e.pdf#page=11"
    defined_for = ProvinceCode.NB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.tuition_amount
        age = person("age", period)
        return age >= p.eligible_age
