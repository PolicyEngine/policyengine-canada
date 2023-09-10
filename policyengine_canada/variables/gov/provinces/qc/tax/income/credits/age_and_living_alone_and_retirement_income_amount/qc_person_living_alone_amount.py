from policyengine_canada.model_api import *


class qc_person_living_alone_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec amount for person living alone"
    definition_period = YEAR
    defined_for = "qc_person_living_alone_eligibility"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.age_and_living_alone_and_retirement_income_amount.living_alone_amount

        # additional amount for a person living alone (single-parent family)
        # TODO: Quebec Amount for Dependants and Amount Transferred by a Child Pursuing Studies > 0 & age <18
        # amount_transfered_from_child_eligible > 0

        # Months in which Family Allowance (FA) is entitled do not qualify for the living alone additional amount (total amount/12)
        # As FA is yearly based, it is assumed that if the full additional amount is to be claimed, then FA cannot be entitled for that year.
        family_allowance_eligible = household("qc_fa_credit", period) <= 0

        additional_amount = p.additional_amount * (
            family_allowance_eligible + amount_transfered_from_child_eligible
        )

        return p.base + additional_amount
