from policyengine_canada.model_api import *


class on_senior_homeowners_property_tax_grant(Variable):
    value_type = float
    entity = Person
    label = "Ontario senior homeowners property tax grant base"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        property_tax_paid = person("property_tax", period)
        age = person("age", period)
        age_eligibility = p.gov.provinces.on.tax.grants.oshtg.age_eligibility
        return property_tax_paid > 0 & age >= age_eligibility
