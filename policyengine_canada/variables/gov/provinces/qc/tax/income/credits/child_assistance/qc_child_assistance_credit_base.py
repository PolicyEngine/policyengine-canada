from policyengine_canada.model_api import *


class qc_child_assistance_credit_base(Variable):
    value_type = float
    entity = Household
    label = "Quebec Child Assitance Tax Credit base amount"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        children = household("qc_child_assistance_credit_children", period)
        p = parameters(period).gov.provinces.qc.tax.income.credits.child_assistance
        return children * p.max_amount