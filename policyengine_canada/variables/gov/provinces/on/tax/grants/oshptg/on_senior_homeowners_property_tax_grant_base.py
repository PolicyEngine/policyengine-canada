from policyengine_canada.model_api import *


class on_senior_homeowners_property_tax_grant_base(Variable):
    value_type = float
    entity = Person
    label = "Ontario senior homeowners property tax grant base"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        property_tax_paid = person("property_tax", period)
        age = person("age", period)
        p = parameters(period).gov.provinces.on.tax.grants.oshptg
        age_eligibility = p.age_eligibility
        eligible = property_tax_paid > 0 & age >= age_eligibility & in_ontario
        max_amount = p.max_amount
        return eligible * min_(property_tax_paid, max_amount)
