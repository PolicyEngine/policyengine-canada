from policyengine_canada.model_api import *


class canada_workers_benefit_disability_supplement_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for canada workers benefit supplement"
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-89.html#docCont"
    )

    def formula(person, period, parameters):
        eligible_person = person("canada_workers_benefit_eligible", period)
        disability_eligible = person("dtc_eligible", period)
        return eligible_person & disability_eligible
