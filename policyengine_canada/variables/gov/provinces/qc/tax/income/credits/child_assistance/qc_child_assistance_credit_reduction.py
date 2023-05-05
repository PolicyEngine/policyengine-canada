from policyengine_canada.model_api import *


class qc_child_assistance_credit_reduction(Variable):
    value_type = float
    entity = Household
    label = "Quebec Child Assitance Tax Credit reduction amount"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        married = household("is_married", period)
        income = household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.child_assistance
        return where(
            married,
            p.couples.phase_out.calc(income),
            p.single_households.phase_out.calc(income),
        )
