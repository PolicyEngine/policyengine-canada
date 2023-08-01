from policyengine_canada.model_api import *


class sk_age_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan age amount credit"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.age_amount
        income = person("individual_net_income", period)
        age = person("age", period)
        eligible = age >= p.age_eligibility
        reduction = p.reduction.rate.calc(income)
        reduced_amount = max_(p.max_amount - reduction, 0)

        return eligible * reduced_amount
