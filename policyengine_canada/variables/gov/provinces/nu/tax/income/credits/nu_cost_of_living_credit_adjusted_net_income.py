from policyengine_canada.model_api import *


class nu_cost_of_living_credit_adjusted_net_income(Variable):
    value_type = float
    entity = Person
    label = "Nunavut adjusted income after armed force and personal deduction"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        armed_deduction = person(
            "canadian_armed_forces_and_personnel_deduction", period
        )
        return max_(0, income - armed_deduction)
