from policyengine_canada.model_api import *


class bc_disability_credit_additional_amount_eligible(Variable):
    value_type = bool
    entity = Person
    label = (
        "Eligible for the British Columbia additional disability tax credit"
    )
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.bc.tax.income.credits.disability
        return person("age", period) < p.additional_amount.age_limit
