from policyengine_canada.model_api import *


class training_credit_income(Variable):
    value_type = float
    entity = Person
    label = "Canada Training Credit Income"
    unit = CAD
    documentation = "This is just net income, which is total income minus all deductions"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        return tax_unit("individual_net_income", period)
  

