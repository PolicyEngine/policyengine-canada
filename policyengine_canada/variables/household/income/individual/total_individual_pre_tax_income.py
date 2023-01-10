from policyengine_canada.model_api import *


class total_individual_pre_tax_income(Variable):
    value_type = float
    entity = Person
    label = "Total Individual Pre Tax Income"
    unit = CAD
    documentation = "Sum of the 5 granular income types, IE employment, self-employment, investment, benefits, and pension-and-savings-plan"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/financial-consumer-agency/services/financial-toolkit/taxes/taxes-2/4.html"

    adds = [
        "benefits_income",
        "employment_income",
        "investment_income",
        "pension_and_savings_plan_income",
        "self_employment_income",
    ]
