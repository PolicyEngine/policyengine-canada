from policyengine_canada.model_api import *


class qc_medical_expenses_spouse_income(Variable):
    value_type = float
    entity = Person
    label = "Quebec medical expenses tax credit spouse income"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        spouse = person("is_spouse", period)
        income = person("individual_net_income", period)

        return spouse * income
