from policyengine_canada.model_api import *


class yt_employment_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon Employment Amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.YT
    reference = "https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc/information-residents-yukon.html#P4_58310"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.employment_amount
        canada_employment_amount = person("canada_employment_amount", period)
        return min_(canada_employment_amount, p.amount)
