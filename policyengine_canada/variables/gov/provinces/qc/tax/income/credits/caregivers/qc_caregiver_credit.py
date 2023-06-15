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

        # Caregiver living with a person 18 or over with an impairment
        eligible_disabled_care_receiver = person(
            "qc_caregiver_living_with_disabled_person_eligibility", period
        )
        #  an additional amount for expenses you incurred for specialized respite services for an eligible care receiver you lived with who is disabled
        specialized_respite_services_expenses = min_(
            person("specialized_respite_services_expenses", period),
            p.specialized_respite_services.expenses_limit,
        )
        specialized_respite_services_credit = (
            p.specialized_respite_services.rate
            * specialized_respite_services_expenses
        )

        credit_living_with_disabled_care_receiver = (
            eligible_disabled_care_receiver
            * (p.credit_amount + specialized_respite_services_credit)
        )

        # Caregiver not living with a person 18 or over with an impairment
        credit_not_living_with_disabled_care_receiver = (
            person(
                "qc_caregiver_not_living_with_disabled_person_eligibility",
                period,
            )
            * p.credit_amount
        )
        # Caregiver living with a person (not his or her spouse) 70 or over without an impairment
        credit_living_with_nondisabled_care_receiver = (
            person(
                "qc_caregiver_living_with_nondisabled_person_eligibility",
                period,
            )
            * p.credit_amount
        )

        return caregiver * (
            credit_living_with_disabled_care_receiver
            + credit_not_living_with_disabled_care_receiver
            + credit_living_with_nondisabled_care_receiver
        )
