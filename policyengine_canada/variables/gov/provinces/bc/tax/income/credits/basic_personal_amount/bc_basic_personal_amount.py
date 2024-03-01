from policyengine_canada.model_api import *


class bc_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "British Columbia basic personal amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1bc/td1bc-23e.pdf#page=1"
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.basic_personal_amount
        return p.base
