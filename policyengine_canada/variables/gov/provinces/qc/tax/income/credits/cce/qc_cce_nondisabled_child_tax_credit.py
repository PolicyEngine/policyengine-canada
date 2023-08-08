from policyengine_canada.model_api import *


class qc_cce_nondisabled_child_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec nondisabled child childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        income = household("adjusted_family_net_income", period)
        credit_rate = p.rate.calc(income)

        person = household.members

        expense = person("childcare_expense", period)
        age = person("age", period)

        expense_limit = p.nondisabled_child_expense_limit.calc(age)

        credit = credit_rate * min_(expense_limit, expense)

        return household.sum(credit)
