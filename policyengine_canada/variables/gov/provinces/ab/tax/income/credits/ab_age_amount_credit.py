from policyengine_canada.model_api import *


class ab_age_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta Age amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.ab_age_amount_credit
        eligible = age >= p.age_eligibility
        income = person("total_individual_pre_tax_income", period)
        base = p.base
        reduction = p.reduction.calc(income)
        return eligible * (max_(0, base - reduction))
