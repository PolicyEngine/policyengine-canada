from policyengine_canada.model_api import *


class slic_base(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan low income tax credit base"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.slic
        children = household("slic_eligible_children", period)
        married = household("is_married", period)
        return (
            p.base.head
            + married * p.base.spouse
            + min_(children * p.base.child, p.child_max_amount)
        )
