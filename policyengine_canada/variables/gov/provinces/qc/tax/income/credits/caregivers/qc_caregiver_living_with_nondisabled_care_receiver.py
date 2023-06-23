from policyengine_canada.model_api import *


class qc_caregiver_living_with_nondisabled_care_receiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax credit for caregivers living with nondisabled care receivers"
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
        # lived together
        cohabiting = person("lived_together", period)

        eligible = (
            nonspouse & nondisabled & care_receiver & age_eligible & cohabiting
        )

        return eligible * p.base_amount
