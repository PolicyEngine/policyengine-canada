from policyengine_canada.model_api import *


class dental_benefit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for dental benefit"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.dental_benefit
        # Determine eligibility.
        has_dental_expenses = person("dental_expenses", period) > 0
        has_private_insurance = person("has_private_dental_insurance", period)
        age_eligible = person("age", period) < p.ineligible_age
        # The amount does not vary with the dental costs.
        # Child only needs to have received some dental care.
        return ~has_private_insurance & has_dental_expenses & age_eligible
