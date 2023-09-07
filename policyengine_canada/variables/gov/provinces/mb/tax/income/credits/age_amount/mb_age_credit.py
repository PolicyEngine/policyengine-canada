from policyengine_canada.model_api import *


class mb_age_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba age credit amount"
    definition_period = YEAR
    defined_for = "mb_age_credit_eligible"
    reference = "https://www.cchwebsites.com/content/pdf/tax_forms/ca/en/td1mbws_en.pdf#page=1"

    def formula(person, period, parameters):
        age = person("age", period)
        income = person("individual_net_income", period)
        p = parameters(period).gov.provinces.mb.tax.income.credits.age_amount
        return max_(p.max_amount - p.phase_out_rate.calc(income), 0)
