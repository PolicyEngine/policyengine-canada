from policyengine_canada.model_api import *


class yt_medical_expense_credit(Variable):
    value_type = float
    entity = Person
    label = "Yukon medical expenses"
    definition_period = YEAR
    defined_for = ProvinceCode.YT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-23e.pdf" # page 23

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        p = parameters(period).gov.provinces.yt.medical
        income_fraction = income * p.rate
        return min_(income_fraction, p.reduction_cap)