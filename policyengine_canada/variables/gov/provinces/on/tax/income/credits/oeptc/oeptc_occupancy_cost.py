from policyengine_canada.model_api import *


class oeptc_occupancy_cost(Variable):
    value_type = float
    entity = Household
    label = "OEPTC occupancy cost"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        property_tax = person("property_tax", period)
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.occupancy_costs
        student_residence = household("lived_in_a_student_residence", period)
        countable_rent = person("rent", period) * p.rent_multiplication_factor
        student_residence_addition = (
            student_residence * p.student_resident_supplement
        )
        return household.sum(
            countable_rent + property_tax + student_residence_addition
        )
