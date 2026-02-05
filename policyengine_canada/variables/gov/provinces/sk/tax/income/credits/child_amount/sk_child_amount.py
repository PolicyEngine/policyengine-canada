from policyengine_canada.model_api import *


class sk_child_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan child amount credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://publications.saskatchewan.ca/api/v1/products/583/formats/806/download#page=16",
    )
    defined_for = "sk_child_amount_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.child_amount
        household = person.household
        count_children = household("sk_count_children", period)
        spouse_income = person("spouse_income", period)
        head_income = person("head_income", period)
        claim = head_income < spouse_income
        #        head_eligible = person("sk_head_eligibility", period)
        #        dependant_eligible = person("sk_dependant_eligibility", period)
        #        eligible = head_eligible * dependant_eligible == 0

        return claim * count_children * p.maximum_child_amount
