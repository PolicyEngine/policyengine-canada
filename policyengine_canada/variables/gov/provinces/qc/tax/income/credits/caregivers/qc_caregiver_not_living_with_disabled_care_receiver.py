from policyengine_canada.model_api import *


class qc_caregiver_not_living_with_disabled_care_receiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax cresit for caregivers not living with disabled care receivers"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers
        # with an impairment
        disabled = person("is_disabled", period)
        # is care receiver
        care_receiver = person("is_care_receiver", period)
        # age eligibility
        age_eligible = person("is_adult", period)
        # lived together
        not_cohabiting = ~person("lived_together", period)

        eligible = disabled & care_receiver & age_eligible & not_cohabiting

        # care giver's income eligibility (line 354)
        income_eligible = max_(
            person("individual_net_income", period) - p.income_limit, 0
        )

        # line 356 - 358
        credit = p.base_amount - min_(income_eligible * p.rate, p.base_amount)

        return eligible * credit
