from policyengine_canada.model_api import *


class benefits_income(Variable):
    value_type = float
    entity = Person
    label = "Benefits income"
    unit = CAD
    documentation = "Income from benefits such as employment insurance and social assistance payments"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-10100-employment-income.html"
