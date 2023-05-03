from policyengine_canada.model_api import *


class sa_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec senior assistance tax credits eligible senior"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        age = person("age", period)

        spouse_eligibility = person("sa_spouse_eligibility", period)

        return (age >= p.age_eligibility) | spouse_eligibility


# todo : considering 3 ways