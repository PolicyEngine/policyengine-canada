from policyengine_canada.model_api import *


class qc_refundable_medical_expense_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec medical expenses tax credit"
    reference = "https://www.revenuquebec.ca/documents/en/formulaires/tp/2022-12/TP-1.D.B-V%282022-12%29.pdf#page=2"
    definition_period = YEAR
    defined_for = "qc_refundable_medical_expense_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses.refundable

        non_refundable_medical_expense = person(
            "qc_non_refundable_medical_expense", period
        )
        disability_supports_expense = person(
            "disability_supports_expense", period
        )
        medical_expense = min_(
            p.rate
            * (non_refundable_medical_expense + disability_supports_expense),
            p.max_amount,
        )

        # reduction
        head_income = person("head_income", period)
        spouse_income = person("spouse_income", period)
        reduction = max_(0, p.reduction.calc(head_income + spouse_income))

        return max_(0, medical_expense - reduction)
