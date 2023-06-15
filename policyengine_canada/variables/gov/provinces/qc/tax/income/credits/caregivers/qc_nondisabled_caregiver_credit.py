from policyengine_canada.model_api import *


class qc_nondisabled_caregiver_credit(Variable):
    value_type = bool
    entity = Person
    label = "Quebec nondisabled caregivers tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregiovers

        # age eligibility
        age_eligible = person("age", period) >= p.age_eligibility
        # lived person eligiblity
        care_receiver = person(
            "qc_nondisabled_caregiver_lived_person_eligibility", period
        )

        return age_eligible * care_receiver * p.credit_amount
