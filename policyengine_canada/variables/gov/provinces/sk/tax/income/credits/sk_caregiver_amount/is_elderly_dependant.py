from policyengine_canada.model_api import *


class is_elderly_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan Caregiver Amount Elderly Dependant"
    documentation = "Whthere your spouse's or common-law partner's dependant is your parent or grandparent or not."
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf""file:///C:/Users/yaoke/OneDrive/Desktop/PolicyEngine/SK/SK%20Tax%20Credit%20Return/td1sk-ws-23e%20(SK%20Tax%20Credit%20Calculation).pdf""file:///C:/Users/yaoke/OneDrive/Desktop/PolicyEngine/SK/SK%20Tax%20Credit%20Return/I2-01.pdf"
    defined_for = ProvinceCode.SK