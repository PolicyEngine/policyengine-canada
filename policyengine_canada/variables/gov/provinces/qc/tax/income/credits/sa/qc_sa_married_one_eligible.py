from policyengine_canada.model_api import *


class qc_sa_married_one_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Quebec senior assistance tax credits for family with only one eligible senior"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        person = household.members

        age_eligible = person("age", period) >= p.age_eligibility
        spouse_eligible = person("qc_sa_spouse_eligible", period)

        return age_eligible ^ spouse_eligible
