from policyengine_canada.model_api import *


class other_employment_income(Variable):
    value_type = float
    entity = Person
    label = "Other employment income"
    unit = CAD
    documentation = "Employment income reported on Line 10400 of the personal income tax return"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-10400-other-employment-income.html"
