from policyengine_canada.model_api import *


class age_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Age amount credit, non-refundable"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.cra.tax.income.credits.age_amount_credit
        eligible = age >= p.age_eligibility
        income = person("total_individual_pre_tax_income", period)
        credit_cap = p.amount.credit_cap
        reduction = p.amount.reduction.calc(income)
        return eligible * (max_(0, credit_cap - reduction))
