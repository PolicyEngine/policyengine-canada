from policyengine_canada.model_api import *


class yt_age_amount_credit_eligible_person(Variable):
    value_type = bool
    entity = Person
    label = "Yukon age amount credit eligible person"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.provinces.yt.tax.income.credits.age_amount
        return age >= p.age_threshold
