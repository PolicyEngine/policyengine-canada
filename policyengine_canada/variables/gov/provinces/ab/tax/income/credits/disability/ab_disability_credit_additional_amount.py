from policyengine_canada.model_api import *


class ab_disability_credit_additional_amount(Variable):
    value_type = float
    entity = Person
    label = "Alberta additional disability tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-22e.pdf#page=2"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ab.tax.income.credits.disability
        childcare_expenses = person("care_expenses", period)
        excess_childcare_expenses = max_(
            0,
            childcare_expenses
            - p.additional_amount.childcare_expense_threshold,
        )
        age = person("age", period)
        additional_amount_base = p.additional_amount.base.calc(age)
        return max_(0, additional_amount_base - excess_childcare_expenses)
