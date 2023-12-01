from policyengine_canada.model_api import *


class qc_caregiver_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec caregivers tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        return person("is_caregiver", period)
