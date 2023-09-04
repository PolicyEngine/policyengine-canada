from policyengine_canada.model_api import *


class qc_cce_disabled_child_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec disabled child childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        income = household("adjusted_family_net_income", period)
        credit_rate = p.rate.calc(income)

        person = household.members

        expense = person("childcare_expense", period)

        individual_income = person("individual_net_income", period)
        own_child = person("is_child_of_filer", period)
        dependant = person("is_dependant", period)
        disabled = person("is_disabled", period)

        qualifying_non_own_child_dependant = dependant & (
            individual_income <= p.child_income_limit
        )
        eligible = disabled & (own_child | qualifying_non_own_child_dependant)

        credit = (
            credit_rate
            * eligible
            * min_(p.disabled_child_expense_limit, expense)
        )

        return household.sum(credit)
