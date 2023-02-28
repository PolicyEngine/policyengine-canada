from policyengine_canada.model_api import *


class eligible_dependent_for_eligible_dependent_amount(Variable):
    value_type = bool
    entity = Person
    label = "Dependent eligible for the eligible dependent amount"
    definition_period = YEAR

    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        age_eligible = (
            person("age", period)
            <= parameters(
                period
            ).gov.cra.tax.income.credits.canada_caregiver_amount.eligible_dependent_amount.age
        )
        return disabled or age_eligible
