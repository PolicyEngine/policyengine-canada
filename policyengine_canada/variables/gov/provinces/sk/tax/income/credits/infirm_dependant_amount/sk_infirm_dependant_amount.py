from policyengine_canada.model_api import *

class sk_infirm_dependant_amount(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Infirm Dependant Amount for Household"
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-23e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-22e.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk-ws/td1sk-ws-lp-22e.pdf#page=6",
        "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=13 #page=14,15",
    )

    adds = ['sk_infirm_dependant_individual_amount"]