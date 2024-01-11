from policyengine_canada.model_api import *


class bc_disability_credit_additional_amount(Variable):
    value_type = float
    entity = Person
    label = "British Columbia additional disability tax credit"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-d/5010-d-22e.pdf#page=1"
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.bc.tax.income.credits.disability
        childcare_expenses = person(
            "childcare_expenses_claimed_by_another_person", period
        )
        reduced_childcare_expenses = max_(
            0, childcare_expenses - p.additional_amount.income_threshold
        )
        age = person("age", period)
        additional_amount_base = (
            p.additional_amount.additional_amount_base.calc(age)
        )
        return max_(0, additional_amount_base - reduced_childcare_expenses)
