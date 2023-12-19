from policyengine_canada.model_api import *


class ab_disability_credit_additional_amount_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the Alberta additional disability tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ab.tax.income.credits.disability
        return person("age", period) < p.additional_amount.age_limit
