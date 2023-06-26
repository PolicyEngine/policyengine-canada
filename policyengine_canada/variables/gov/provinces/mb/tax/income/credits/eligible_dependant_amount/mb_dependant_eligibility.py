from policyengine_canada.model_api import *


class mb_dependant_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba dependant eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        # eligible dependant condition 2

        relative = person("is_relative", period)
        live_together = person("lived_together", period)

        dependant_eligible = relative & live_together

        return dependant_eligible
