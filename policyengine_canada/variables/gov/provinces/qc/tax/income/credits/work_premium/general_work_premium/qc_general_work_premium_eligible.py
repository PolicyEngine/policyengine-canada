from policyengine_canada.model_api import *


class qc_general_work_premium_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Quebec general work premium tax credit eligibility"
    definition_period = YEAR
    defined_for = "qc_work_premium_eligible"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.general_work_premium

        married = household("is_married", period)

        working_income = household("family_working_income", period)
        return where(
            married,
            working_income > p.couple.work_income_requirement,
            working_income > p.single.work_income_requirement,
        )
