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
        reduction = (
            (income > p.net_income_base_amount)
            * (income - p.net_income_base_amount)
            * p.reduction_rate
        )
        reduced_amount = p.maximum_age_amount - reduction

        return max_(0, eligible * reduced_amount)
