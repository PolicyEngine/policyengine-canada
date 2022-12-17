from policyengine_canada.model_api import *


class canada_workers_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit"
    definition_period = YEAR

    def formula(household, period, parameters):
        formula = sum_of_variables(
            "canada_workers_benefit_base", "canada_workers_benefit_supplement"
        )

        # Grab working income. (maybe could be its own variable)
        # -> Add a parameter listing working income sources (employment + self-employment)
        # Compute phase-in amount using the scale parameter
        # Compute the max amount (including supplement).
        # -> Substep: Are they family? How many people with disabilities? (both or one)
        # --> Subsubstep: Number of dependents
        # ---> I think cwb_dependant == ~cwb_eligible?
        # Compute the phase-out amount
        # return min_(max_(amount - phase_out, 0), phase_in)
