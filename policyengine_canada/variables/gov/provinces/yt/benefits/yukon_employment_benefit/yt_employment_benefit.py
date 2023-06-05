from policyengine_canada.model_api import *


class yt_employment_benefit(Variable):
    value_type = float
    entity = Person
    label = "Yukon Employment Amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.YT
    reference = "https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc/information-residents-yukon.html#P4_58310"

    def formula(person, period, parameters):
        maximun_return_amount = parameters(
            period
        ).gov.provinces.yt.benefits.employment_benefit

        employment_income = person("employment_income", period)

        return min_(employment_income, maximun_return_amount)
