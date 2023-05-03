from policyengine_canada.model_api import *


class qc_child_assistance_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec Child Assitance Tax Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        base = household("qc_child_assistance_credit_base", period)
        reduction = household("qc_child_assistance_credit_reduction", period)
        children = household("qc_child_assistance_credit_children", period)
        p = parameters(period).gov.provinces.qc.tax.income.credits.child_assistance
        minimum_amount = children * p.min_amount
        supplement = household("qc_child_assistance_credit_supplement", period)
        back_to_school = household("qc_child_assistance_credit_back_to_school_amount", period)
        amount = max_(minimum_amount, base - reduction)
        return amount + supplement + back_to_school
