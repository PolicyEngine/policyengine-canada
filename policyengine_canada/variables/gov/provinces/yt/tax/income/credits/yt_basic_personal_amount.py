from policyengine_canada.model_api import *


class yt_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon basic personal amount"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.basic_personal_amount
        exceedance = income - p.income_threshold
        eligible = exceedance >= 0
        percent = max_(0, (p.scale_value - exceedance) / p.scale_value)
        return (percent * p.applicable_amount + p.base_amount) * eligible
