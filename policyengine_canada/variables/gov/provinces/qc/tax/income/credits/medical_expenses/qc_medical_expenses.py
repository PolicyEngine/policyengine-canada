from policyengine_canada.model_api import *


class qc_medical_expenses(Variable):
    value_type = float
    entity = Person
    label = "Quebec medical expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.medical_expenses

        medical_expenses = person("medical_expenses", period)

        # age eligibility
        age_eligible = person("age", period) >= p.age_eligibility

        # work income eligibility
        work_income_eligible = (
            person("working_income", period) >= p.work_income_base
        )

        # compare family income with maximum family income
        income = person("individual_net_income", period)
        spouse_income = person("spouse_income", period)
        family_income_eligible = (
            income + spouse_income
        ) < p.maximum_family_income.calc(medical_expenses)

        eligible = age_eligible * work_income_eligible * family_income_eligible

        return eligible * medical_expenses
