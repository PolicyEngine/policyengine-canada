from policyengine_canada.model_api import *


class dependant_age(Variable):
    value_type = int
    entity = Person
    label = "Saskatchewan Caregiver Amount Dependant's Age"
    documentation = "The age of your spouse's or common-law partner's parent or grandparent or an infirm relative."
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf""file:///C:/Users/yaoke/OneDrive/Desktop/PolicyEngine/SK/SK%20Tax%20Credit%20Return/td1sk-ws-23e%20(SK%20Tax%20Credit%20Calculation).pdf""file:///C:/Users/yaoke/OneDrive/Desktop/PolicyEngine/SK/SK%20Tax%20Credit%20Return/I2-01.pdf"
    defined_for = ProvinceCode.SK