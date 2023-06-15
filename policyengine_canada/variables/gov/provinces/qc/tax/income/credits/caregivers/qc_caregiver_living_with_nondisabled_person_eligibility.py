from policyengine_canada.model_api import *


class qc_caregiver_living_with_nondisabled_person_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec eligibility for care receivers living with nondisabled caregivers"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers
        # not his or her spouse
        nonspouse = ~person("is_spouse", period)
        # without an impairment
        nondisabled = ~person("is_disabled", period)
        # is care receiver
        care_receiver = person("is_care_receiver", period)
        # age eligibility
        age_eligible = person("age", period) >= p.age_eligibility

        return nonspouse * nondisabled * care_receiver * age_eligible
