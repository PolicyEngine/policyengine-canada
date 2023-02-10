from policyengine_canada.model_api import *


class on_low_income_workers_tax_credit_base(Variable):
    value_type = float
    entity = Person
    label = "Base amount of Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        employment_income = person("employment_income", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.lift
        eligible_people = person(
            "on_low_income_workers_tax_credit_eligible_people", period
        )
        return min_(
            eligible_people * p.amount,
            employment_income * p.phase_in_rate,
        )
