from policyengine_canada.model_api import *


class qc_disability_supports_expense(Variable):
    value_type = float
    entity = Person
    label = "Disability Supports Expense"
    definition_period = YEAR
    defined_for = ProvinceCode.QC
