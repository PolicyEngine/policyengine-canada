from policyengine_canada.model_api import *


class sa_spouse_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec senior assistance tax credits eligible senior's spouse"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        age = person("age", period)
        spouse = person("is_spouse", period)

        return spouse & (age >= p.age_eligibility)


        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        age_eligible = person("age", period) >= p.age_eligibility

        spouse = person("is_spouse", period)

        return age_eligible & (spouse)