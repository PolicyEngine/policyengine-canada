from policyengine_canada.model_api import *


class canada_pension_plan(Variable):
    value_type = float
    entity = Person
    label = "Canada Pension Plan Contribution"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, paramaters):
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        p = paramaters(period).gov.cra.CPP
        employment_eligibility = employment_income > p.min_income
        self_employment_eligibility = self_employment_income > p.min_income
        employment_contribution = employment_eligibility * min_(
            p.employed.rate.calc(employment_income),
            p.employed.max_contribution,
        )
        self_employment_contribution = self_employment_eligibility * min_(
            p.self_employed.rate.calc(self_employment_income),
            p.self_employed.max_contribution,
        )
        return employment_contribution + self_employment_contribution
