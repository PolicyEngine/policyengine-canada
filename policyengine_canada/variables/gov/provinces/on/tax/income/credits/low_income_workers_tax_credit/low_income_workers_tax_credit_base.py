from policyengine_canada.model_api import *


class low_income_workers_tax_credit_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount of Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        family_employment_income = household(
            "family_employment_income", period
        )
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.low_income_workers_tax_credit
        eligible = household("low_income_workers_tax_credit_eligible", period)
        amount = min_(p.amount, family_employment_income * p.rate)
        return max_(amount, 0)
