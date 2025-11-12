from policyengine_canada.model_api import *


class mb_dependant_amount_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba head of household eligibility"
    definition_period = YEAR
    defined_for = "mb_dependant_amount_eligibile_dependant"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        #  do not have a spouse or common-law partner, or you have a spouse or common-law partner who does not live with you and who you are not supporting or being supported by
        has_spouse = person("is_spouse", period)

        not_live_together = ~person("lived_together", period)
        not_care_receiver = ~person("is_care_receiver", period)
        not_care_giver = ~person("is_caregiver", period)

        spouse_eligible = (
            has_spouse & not_live_together & not_care_receiver & not_care_giver
        )

        head_eligibility = ~has_spouse | spouse_eligible

        return head_eligibility
