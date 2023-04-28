from policyengine_canada.model_api import *


class qc_child_assistance_credit_back_to_school_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec Child Assitance Tax Credit back to school amount"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        person = household.members
        child = person("qc_child_assistance_credit_child", period)
        in_school = person("is_of_school_age", period)
        eligible = child & in_school
        p = parameters(period).gov.provinces.qc.tax.income.credits.child_assistance
        return eligible * p.qc_child_assistance_credit_back_to_school_amount
