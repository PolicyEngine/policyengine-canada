from policyengine_canada.model_api import *


class mb_dependant_eligibility(Variable):
    value_type = float
    entity = Person
    label = "Manitoba eligible dependant amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        # eligible dependent condition 2

        relative = person("is_relative", period)
        live_together = person("lived_together", period)
        
        # eligible dependent condition 3

        income = person("individual_net_income", period)
        income_eligible = income < p.dependant_income_max_amount

        dependant_eligible = relative & live_together & income_eligible

        return dependant_eligible