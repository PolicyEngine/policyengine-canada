from policyengine_canada.model_api import *


class spouse_spa_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Spouse is eligible for the Spousal Allowance"
    definition_period = YEAR

    def formula(person, period, parameters):
        spa_eligible = person("spa_eligible", period)
        head_or_spouse = person("is_head", period) | person(
            "is_spouse", period
        )
        head_or_spouse_spa_eligible = head_or_spouse & spa_eligible
        household = person.household
        count_head_or_spouse_spa_eligible = household.sum(
            head_or_spouse_spa_eligible
        )

        return count_head_or_spouse_spa_eligible - where(spa_eligible, 1, 0)
