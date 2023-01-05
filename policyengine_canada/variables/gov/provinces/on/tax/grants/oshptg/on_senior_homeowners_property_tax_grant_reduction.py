from policyengine_canada.model_api import *


class on_senior_homeowners_property_tax_grant_reduction(Variable):
    value_type = float
    entity = Person
    label = "Ontario senior homeowners property tax grant reduction"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person.household("adjusted_family_net_income", period)
        married = person.household("is_married", period)
        p = parameters(period).gov.provinces.on.tax.grants.oshptg.reduction
        return where(married, p.family.calc(income), p.single.calc(income))
