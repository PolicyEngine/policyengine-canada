from policyengine_canada.model_api import *


class qc_caregiver_living_with_disabled_person_eligibility(Variable):
    value_type = bool
    entity = Person
    label = (
        "Quebec eligibility for care receivers living with disabled caregivers"
    )
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
        cohabiting = person("lived_together", period)

        return disabled * care_receiver * age_eligible * cohabiting
