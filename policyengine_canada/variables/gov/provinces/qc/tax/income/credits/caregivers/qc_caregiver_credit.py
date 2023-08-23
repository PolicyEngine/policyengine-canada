from policyengine_canada.model_api import *


class qc_caregiver_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregivers tax credit"
    definition_period = YEAR
    defined_for = "qc_caregiver_eligibility"

    adds = [
        "qc_caregiver_living_with_disabled_carereceiver",
        "qc_caregiver_not_living_with_disabled_carereceiver",
        "qc_caregiver_living_with_nondisabled_carereceiver",
    ]
