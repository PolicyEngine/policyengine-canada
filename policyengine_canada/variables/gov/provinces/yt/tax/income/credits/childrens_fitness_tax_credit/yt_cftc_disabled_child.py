from policyengine_canada.model_api import *


class yt_cftc_disabled_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon Child Fitness Tax Credit disabled child"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        fees = person("physical_activities_fees", period)
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_fitness.disability_supplement
        return (fees >= p.minimum_fees) & disabled & (age < p.age)
