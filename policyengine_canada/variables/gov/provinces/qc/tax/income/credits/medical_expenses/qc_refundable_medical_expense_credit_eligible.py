from policyengine_canada.model_api import *


class qc_refundable_medical_expense_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Quebec refundable medical expenses tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses.refundable.eligibility

        # age eligibility
        age_eligible = person("age", period) >= p.age

        # work income eligibility
        work_income_eligible = (
            person("working_income", period) >= p.work_income
        )

        # non-refundable medical expense eligibility
        non_refundable_medical_expense_eligible = (
            person("qc_non_refundable_medical_expense", period) > 0
        )

        return (
            age_eligible
            & work_income_eligible
            & non_refundable_medical_expense_eligible
        )
