from policyengine_canada.model_api import *


class mb_dependant_amount_eligibile_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba dependant eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        # eligible dependant is related to you and lives with you

        relative = person("is_relative", period)
        live_together = person("lived_together", period)

        # eligible dependant's net income

        dependant_income = person("dependant_income", period)
        eligible_dependant_income = (
            p.dependant_income_max_amount > dependant_income
        )

        dependant_eligible = (
            relative & live_together & eligible_dependant_income
        )

        return dependant_eligible
