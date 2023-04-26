from policyengine_canada.model_api import *


class cce_nondisabled_children_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec childcare tax credit for nondisabled children"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce
        eligible_nondisabled_children = household(
            "cce_eligible_nondisabled_children", period
        )
        expenses = household("childcare_expenses", period)
        return
