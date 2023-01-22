from policyengine_canada.model_api import *


class training_credit_income(Variable):
    value_type = float
    entity = Person
    label = "Canada Training Credit Income"
    unit = CAD
    documentation = "The sum of employment income, self-employment income, maternity benefits and parental benefits"
    definition_period = YEAR

    formula = sum_of_variables(
        "gov.cra.tax.income.credits.training.income_sources"
    )
