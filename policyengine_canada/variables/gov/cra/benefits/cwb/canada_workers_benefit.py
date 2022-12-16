from policyengine_canada.model_api import *


class canada_workers_benefit(Variable):
    value_type = bool
    entity = Household
    label = "Canada workers benefit"
    definition_period = YEAR

    def formula(household, period, parameters):
        # Grab working income. (maybe could be its own variable)
        # -> Add a parameter listing working income sources (employment + self-employment)
        # Compute phase-in amount using the scale parameter
        # Compute the max amount (including supplement).
        # -> Substep: Are they family? How many people with disabilities? (both or one)
        # --> Subsubstep: Number of dependents
        # ---> I think cwb_dependant == ~cwb_eligible?
        # Compute the phase-out amount
        # return min_(max_(amount - phase_out, 0), phase_in)


    # Variable structure (household unless otherwise specified):
    # canada_workers_benefit
    # - canada_workers_benefit_base
    # - canada_workers_benefit_disability_supplement
    # - cwb_category (individual/family)
    # - cwb_working_income
    # - cwb_disability_category (none/one/both)
    # - cwb_eligible (person)
    # - cwb_dependent (person)
    # CHECK: Do basic and supplements phase in together?