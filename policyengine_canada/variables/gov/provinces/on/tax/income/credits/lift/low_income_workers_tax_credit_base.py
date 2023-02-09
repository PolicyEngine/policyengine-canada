from policyengine_canada.model_api import *


class low_income_workers_tax_credit_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount of Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        province = household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        employment_income = household("family_employment_income", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.lift
        eligible_people = household(
            "low_income_workers_tax_credit_eligible_people", period
        )
        amount = min_(
            eligible_people * p.amount,
            employment_income * p.phase_in_rate,
        )
        return in_ontario * amount
