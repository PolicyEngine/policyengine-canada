from policyengine_canada.model_api import *


class cwb_disability_supplement_max_amount(Variable):
    value_type = float
    entity = Household
    label = "Eligible for canada workers benefit supplement"
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-89.html#docCont"
    )

    def formula(household, period, parameters):
        person = household.members
        eligible = person("cwb_disability_supplement_eligible", period)
        amount = parameters(
            period
        ).gov.cra.benefits.cwb.amount.disability_supplement
        return household.sum(eligible * amount)
