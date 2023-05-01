from policyengine_canada.model_api import *


class qc_child_assistance_credit_supplement(Variable):
    value_type = float
    entity = Household
    label = "Quebec Child Assitance Tax Credit single household supplement"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        married = household("is_married", period)
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.qc.tax.income.credits.child_assistance.single_households.supplement
        children = household("qc_child_assistance_credit_children", period)
        eligible = ~married & (children > 0)
        reduced_amount = p.max_amount - p.phase_out.calc(income)
        return eligible * (max_(reduced_amount, p.min_amount))

