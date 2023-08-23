from policyengine_canada.model_api import *


class qc_medical_expense_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec medical expenses tax credit"
    definition_period = YEAR
    defined_for = "qc_medical_expense_credit_eligible"

    def formula(person, period, parameters):
        medical_expenses = person("medical_expenses", period)
        return medical_expenses
