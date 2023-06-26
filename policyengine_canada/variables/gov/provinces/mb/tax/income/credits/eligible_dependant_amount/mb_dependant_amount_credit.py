from policyengine_canada.model_api import *


class mb_eligible_dependant_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba eligible dependant amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        # eligible dependent condition 1
        no_spouse = ~person('is_spouse', period)

        has_spouse = person("is_spouse", period)
        not_live_together = ~person("lived_together", period)
        not_care_receiver = ~person("is_care_receiver", period)
        not_care_giver = ~person("is_caregiver", period)

        spouse_eligible = has_spouse & not_live_together & not_care_receiver & not_care_giver

        head_eligibility = no_spouse | spouse_eligible
        

        credit = head_eligibility * person("mb_dependant_eligibility", period) * (p.max_amount - income)

        return credit