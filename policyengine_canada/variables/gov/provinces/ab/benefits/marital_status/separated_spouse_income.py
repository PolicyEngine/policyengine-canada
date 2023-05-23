from policyengine_canada.model_api import *


class separated_spouse_income(Variable):
    value_type = float
    entity = Person
    label = "Spouse income after separating from head of household"
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        filing_status = household("filing_status", period)
        status = filing_status.possible_values
        spouse = person("is_spouse", period)
        income = person("individual_net_income", period)
        return spouse * where(filing_status == status.SEPARATE, income , 0)
