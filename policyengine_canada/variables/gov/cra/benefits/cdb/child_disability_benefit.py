from policyengine_canada.model_api import *


class child_disability_benefit(Variable):
    value_type = float
    entity = Household
    label = "Child Disability Benefit"
    unit = CAD
    documentation = "Non taxable amount paid monthly per children with a severe and prolonged impairment in physical or mental functions."
    definition_period = YEAR

    def formula(household, period, parameters):
        reduction = household("child_disability_benefit_reduction", period)
        base = parameters(period).gov.cra.benefits.cdb.base
        children = household("child_disability_benefit_children", period)
        return max_(base * children - reduction, 0)
