from policyengine_canada.model_api import *


class sk_child_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan child amount credit"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.child_amount
        household = person.household
        count_children = household("sk_count_children", peroid)
        spouse_income = person("spouse_income", period)
        head_income = person("individual_net_income", period)
        eligible = head_income < spouse_income

        return eligible * count_children * p.maximum_child_amount
