from policyengine_canada.model_api import *


class sa_individual_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec senior assistance tax credits for family with only one eligible senior"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        age_eligible = person("age", period) >= p.age_eligibility
        spouse_eligibility = person("sa_spouse_eligibility", period)

        eligible = age_eligible ^ spouse_eligibility

        return household.any(eligible)
