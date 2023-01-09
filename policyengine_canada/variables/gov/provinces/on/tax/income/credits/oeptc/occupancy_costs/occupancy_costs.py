from policyengine_canada.model_api import *


class occupancy_costs(Variable):
    value_type = float
    entity = Household
    label = "Oeptc occupancy costs"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        property_tax = person("property_tax", period)
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.occupancy_costs
        student_residence = person("lived_in_a_student_residence", period)
        rent_multiplication = person("rent", period) * p.multiplication_factor
        student_residence_addition = (
            student_residence * p.student_resident_supplement
        )
        return rent_multiplication + property_tax + student_residence_addition


# TODO: simplify
