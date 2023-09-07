from policyengine_canada.model_api import *


class nu_age_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Nunavut age amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "nu_age_amount_credit_eligible"

    def formula(person, period, parameters):
        income = person("total_individual_pre_tax_income", period)
        p = parameters(period).gov.provinces.nu.tax.income.credits.age_amount
        phase_out_amount = p.phase_out_rate.calc(income)
        return max_(p.amount - phase_out_amount, 0)
