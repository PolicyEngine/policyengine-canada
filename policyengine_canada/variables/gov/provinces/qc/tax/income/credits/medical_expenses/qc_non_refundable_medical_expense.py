from policyengine_canada.model_api import *


class qc_non_refundable_medical_expense(Variable):
    value_type = float
    entity = Person
    label = "Quebec non-refundable medical expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses.non_refundable

        medical_expense = person("medical_expenses", period)

        # the sum of your /and your spouses income
        head_income = person("head_income", period)
        spouse_income = person("spouse_income", period)
        reduction = p.reduction_rate * (head_income + spouse_income)

        return max_(0, medical_expense - reduction)
