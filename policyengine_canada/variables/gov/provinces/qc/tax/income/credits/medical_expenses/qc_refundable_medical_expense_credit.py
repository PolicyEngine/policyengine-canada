from policyengine_canada.model_api import *


class qc_refundable_medical_expense_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec medical expenses tax credit"
    reference = "https://www.revenuquebec.ca/documents/en/formulaires/tp/2022-12/TP-1.D.B-V%282022-12%29.pdf#page=2"
    definition_period = YEAR
    defined_for = "qc_refundable_medical_expense_credit_eligible"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses.refundable

        non_refundable_medical_expense = household(
            "qc_non_refundable_medical_expense", period
        )
        disability_support_expenses = add(
            household, period, ["disability_support_expenses"]
        )

        medical_expense = p.rate * (
            non_refundable_medical_expense + disability_support_expenses
        )
        refundable_medical_expense = min_(medical_expense, p.max_amount)

        # reduction
        family_income = household("qc_family_income", period)
        reduction = max_(0, p.reduction.calc(family_income))

        return max_(0, refundable_medical_expense - reduction)
