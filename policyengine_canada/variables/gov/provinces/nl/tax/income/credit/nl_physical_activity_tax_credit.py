from policyengine_canada.model_api import *


class nl_physical_activity_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Newfoundland Physical activity tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nl.tax.income.credits.physical_activity

        # Person has to be either head, spouse or child under 18 to be eligible.
        eligible = (
            person("is_head", period)
            | person("is_spouse", period)
            | (person("age", period) < p.age_eligible)
        )

        individual_expenses = eligible * (
            person("physical_activities_fees", period)
        )

        expenses = household.sum(individual_expenses)
        maximum_amount = min_(expenses, p.max_amount)

        return maximum_amount * p.rate
