from policyengine_canada.model_api import *


class mb_head_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba head of household eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        # eligible dependant condition 1
        no_spouse = ~person("is_spouse", period)

        has_spouse = person("is_spouse", period)
        not_live_together = ~person("lived_together", period)
        not_care_receiver = ~person("is_care_receiver", period)
        not_care_giver = ~person("is_caregiver", period)

        spouse_eligible = (
            has_spouse & not_live_together & not_care_receiver & not_care_giver
        )

        head_eligibility = no_spouse | spouse_eligible

        # eligible dependant condition 3
        dependant_income_eligibility = (
            person("dependant_income", period) < p.dependant_income_max_amount
        )

        eligibility = head_eligibility & dependant_income_eligibility

        return eligibility
