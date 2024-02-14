from policyengine_canada.model_api import *


class qc_non_refundable_medical_expense(Variable):
    value_type = float
    entity = Household
    label = "Quebec non-refundable medical expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses.non_refundable

        medical_expense = add(household, period, ["medical_expenses"])

        # reduction
        family_income = household("qc_family_income", period)
        reduction = p.income_floor * family_income

        return max_(0, medical_expense - reduction)
