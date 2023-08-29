from policyengine_canada.model_api import *


class qc_caregiver_living_with_nondisabled_carereceiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax credit for caregivers living with nondisabled care receivers"
    definition_period = YEAR
    defined_for = "qc_caregiver_living_with_nondisabled_carereceiver_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers
        return p.base_amount
