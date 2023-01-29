from policyengine_canada.model_api import *


class is_child_for_bc_climate_action_tax_credit(Variable):
    value_type = bool
    entity = Person
    label = "Is the first born child in a Household"
    definition_period = YEAR
    defined_for = "is_dependent"

    def formula(person, period, parameters):
        adult_age = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.bccatc.adult_age
        return person("age", period) < adult_age
        # The definition of an eligible child also includes living with
        # parents and eligibilty under CCB. These are not included here.
