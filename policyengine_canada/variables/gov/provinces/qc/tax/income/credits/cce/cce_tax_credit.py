from policyengine_canada.model_api import *


class cce_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        income = household("adjusted_family_net_income", period)
        credit_rate = p.rate.calc(income)

        expenses = household("childcare_costs", period)

        eligible_nondisabled_young_children = household(
            "cce_eligible_nondisabled_young_children", period
        )
        eligible_nondisabled_old_children = household(
            "cce_eligible_nondisabled_old_children", period
        )
        eligible_disabled_children = household(
            "cce_eligible_disabled_children", period
        )
        expense_limit = (
            eligible_nondisabled_young_children
            * p.nondisabled_young_child_expense_limit
            + eligible_nondisabled_old_children
            * p.nondisabled_old_child_expense_limit
            + eligible_disabled_children * p.disabled_child_expense_limit
        )
        return credit_rate * min_(expenses, expense_limit)
