from policyengine_canada.model_api import *


class sk_low_income_credit_base(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan low income tax credit base"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.slic
        children = household("sk_low_income_credit_eligible_children", period)
        married = household("is_married", period)
        maximum_amount = p.child.max_number * p.child.amount
        return (
            p.head
            + married * p.spouse
            + min_(children * p.child.amount, maximum_amount)
        )
