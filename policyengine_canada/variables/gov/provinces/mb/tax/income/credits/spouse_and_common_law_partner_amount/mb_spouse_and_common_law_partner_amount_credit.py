from policyengine_canada.model_api import *


class mb_spouse_and_common_law_partner_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba spouse and commonlaw partner amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):

        spouse_income = person("spouse_income", period)
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.spouse_and_common_law_partner_amount
        return max_(0, (p.base - spouse_income))
