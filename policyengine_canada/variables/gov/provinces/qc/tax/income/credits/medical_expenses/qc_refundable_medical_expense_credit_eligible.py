from policyengine_canada.model_api import *


class qc_refundable_medical_expense_credit_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Quebec refundable medical expenses tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses.refundable.eligibility

        person = household.members
        is_head = person("is_head", period)

        # age eligibility
        age_eligible = person("age", period) >= p.age

        # work income eligibility
        work_income_eligible = (
            person("working_income", period) >= p.work_income
        )

        eligibility = household.any(
            is_head & age_eligible & work_income_eligible
        )

        # non-refundable medical expense eligibility
        non_refundable_medical_expense_eligible = (
            household("qc_non_refundable_medical_expense", period) > 0
        )

        # family income eligibility
        family_income_eligible = (
            household("qc_family_income", period) <= p.family_income
        )

        return (
            eligibility
            & non_refundable_medical_expense_eligible
            & family_income_eligible
        )
