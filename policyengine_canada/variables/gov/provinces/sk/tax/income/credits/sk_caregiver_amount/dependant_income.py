from policyengine_canada.model_api import *


class dependant_income(Variable):
    value_type = float
    entity = Person
    label = "Dependant Income"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-lp-22e.pdf#page=5",
        "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=13",  # page=14,16,17
    )
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        dependant = person("is_dependant", period)
        income = person("individual_net_income", period)
        return dependant * income
