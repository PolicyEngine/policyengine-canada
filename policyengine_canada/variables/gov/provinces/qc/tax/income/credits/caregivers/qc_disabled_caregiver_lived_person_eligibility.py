from policyengine_canada.model_api import *


class qc_disabled_caregiver_lived_person_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec eligibility for people living with disabled caregivers"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregiovers
        # with an impairment
        disabled = person("is_disabled", period)
        # is care receiver
        care_receiver = person("is_care_receiver", period)
        # age eligibility
        age_eligible = person("is_adult", period)

        return disabled * care_receiver * age_eligible
