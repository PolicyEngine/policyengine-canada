from policyengine_canada.model_api import *


class yt_basic_amount_cal(Variable):
    value_type = float
    entity = Person
    label = "Yukon Basic Amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1yt-ws/td1yt-ws-23e.pdf"
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        income = person("yt_taxable_income", period)

        p = parameters(period).gov.provinces.yt.tax
        amount = p.amount
        applicable_amount = p.basic_personal_amount.applicable_amount
        base_amount = p.basic_personal_amount.base_amount
        checking_point = p.basic_personal_amount.checking_point
        income_threshold = p.basic_personal_amount.income_threshold

        check1 = checking_point - (income - income_threshold)

        result = 13521

        if check1 > 0:
            result = result + (applicable_amount * (check1 / checking_point))

        return result
