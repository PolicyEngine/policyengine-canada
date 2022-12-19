from policyengine_canada.model_api import *


class canada_workers_benefit_disability_supplement_max_amount(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for canada workers benefit supplement"
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-89.html#docCont"
    )

    def formula(person, period, parameters):
        return parameters(period).benefit.canada_workers_benefit.max_amount
