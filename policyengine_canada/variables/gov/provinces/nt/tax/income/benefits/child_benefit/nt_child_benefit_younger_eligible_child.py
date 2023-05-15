from policyengine_canada.model_api import *


class nt_child_benefit_younger_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for the Northwest Territories Child Benefit in the younger bracket"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.benefits.child_benefit.younger
        age = person("age", period)
        return p.age_eligibility > age
