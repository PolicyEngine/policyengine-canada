from policyengine_canada.model_api import *


class yt_cftc_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon Normal Fitness Fee eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_fitness
        disabled = person("is_disabled", period) & (
            age < p.disability_supplement.age
        )
        return disabled | (age < p.child_age_eligibility)
