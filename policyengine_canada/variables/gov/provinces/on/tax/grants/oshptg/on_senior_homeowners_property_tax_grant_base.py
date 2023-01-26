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
        p = parameters(period).gov.provinces.on.tax.grants.oshptg
        age_eligible = person("age", period) >= p.age_eligibility
        eligible = age_eligible & in_ontario
        amount_if_eligible = min_(person("property_tax", period), p.max_amount)
        return eligible * amount_if_eligible
