from policyengine_canada.model_api import *


class yt_employment_benefit(Variable):
    value_type = float
    entity = Person
    label = "Yukon Employment Amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.YT
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31260-canada-employment-amount.html"

    def formula(household, period, parameters):
        income = parameters(period).gov.provinces.yt.benefits.employment_benefit
         
        benefits_income = household("benefits_income", period)

        return min_(benefits_income, income)

