from policyengine_canada.model_api import *


class qc_caregiver_living_with_disabled_carereceiver_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Quebec caregiver tax credit for caregivers living with disabled care receivers eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers
        # with an impairment
        disabled = person("is_disabled", period)
        # is care receiver
        carereceiver = person("is_carereceiver", period)
        # age eligibility
        age_eligible = person("age", period) >= p.eligibility.carereceiver_age
        # lived together
        cohabiting = person("lived_together", period)

        return disabled & carereceiver & age_eligible & cohabiting
