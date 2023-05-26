from policyengine_canada.model_api import *


class eligible_dependent_for_canada_caregiver_amount(Variable):
    value_type = bool
    entity = Person
    label = "Dependent eligible for the Canada caregiver amount"
    definition_period = YEAR

    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        age_eligible = (
            person("age", period)
            >= parameters(
                period
            ).gov.cra.tax.income.credits.canada_caregiver_amount.age_eligibility
        )
        return disabled & age_eligible
