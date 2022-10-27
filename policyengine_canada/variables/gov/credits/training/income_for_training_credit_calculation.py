from policyengine_canada.model_api import *


class income_for_training_credit_calculation(Variable):
    value_type = float
    entity = Person
    label = "Canada Training Credit Income"
    unit = CAD
    documentation = "The sum of employment income, self-employment income, maternity benefits and parental benefits"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):

        income = sum_of_variables(
            ["employment_income", "self_employment_income"]
        )

    # TODO: add maternity income
