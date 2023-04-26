from policyengine_canada.model_api import *


class cce_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce
        age = person("age", period)

        income = household("adjusted_family_net_income", period)
        credit_rate = p.rate.calc(income)

        expenses = person("childcare_expenses", period)

        eligible_nondisabled_children = household(
            "cce_eligible_nondisabled_children", period
        )
        eligible_disabled_children = household(
            "cce_eligible_disabled_children", period
        )

        return eligible_disabled_children * min_(
            expenses * credit_rate, p.disabled_child_credit_limit
        ) + eligible_nondisabled_children * min_(
            expenses * credit_rate, p.nondisabled_child_credit_limit.calc(age)
        )

# todo: separate the nondisable and disable, then add[]
