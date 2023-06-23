from policyengine_canada.model_api import *


class sk_age_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan Personal Tax Credits Return Age Amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.credits_return.amount.age
        income = person("individual_net_income", period)
        age = person("age", period)
        eligible = age >= p.age_eligibility
        reduction = (
            (income > p.net_income_base_amount)
            * (income - p.net_income_base_amount)
            * p.reduction_rate
        )

        return (
            eligible
            * (income < p.net_income_maximum_amount)
            * (p.age_amount - reduction)
        )

    # enter = age_amount - [(income - lower_threshold) * reduction_rate]
    # enter = 5_380 - (income - 40_051) * 0.15
