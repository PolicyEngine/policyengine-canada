from policyengine_canada.model_api import *


class qc_caregiver_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregivers tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers

        caregiver = person("is_caregiver", period)

        credit_living_with_disabled_care_receiver = person(
            "qc_caregiver_living_with_disabled_care_receiver", period
        )
        credit_not_living_with_disabled_care_receiver = person(
            "qc_caregiver_not_living_with_disabled_care_receiver", period
        )
        credit_living_with_nondisabled_care_receiver = person(
            "qc_caregiver_living_with_nondisabled_care_receiver", period
        )

        return caregiver * (
            credit_living_with_disabled_care_receiver
            + credit_not_living_with_disabled_care_receiver
            + credit_living_with_nondisabled_care_receiver
        )
