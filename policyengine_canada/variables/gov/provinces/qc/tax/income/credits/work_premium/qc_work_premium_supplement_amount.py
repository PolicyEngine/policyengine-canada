from policyengine_canada.model_api import *


class qc_work_premium_supplement_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec supplement to the work premium"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.supplement

        person = household.members
        work_income_eligible = (
            person("working_income", period) > p.work_income_eligibility
        )
        supplement_eligible = household.sum(work_income_eligible)

        return select(
            [supplement_eligible == 2, supplement_eligible == 1],
            [p.amount.couple, p.amount.single],
            default=0,
        )
