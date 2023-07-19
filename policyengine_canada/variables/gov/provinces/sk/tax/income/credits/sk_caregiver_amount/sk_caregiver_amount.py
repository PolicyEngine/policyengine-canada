from policyengine_canada.model_api import *


class sk_caregiver_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan Caregiver Amount"
    unit = CAD
    definition_period = YEAR
   reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf""file:///C:/Users/yaoke/OneDrive/Desktop/PolicyEngine/SK/SK%20Tax%20Credit%20Return/td1sk-ws-23e%20(SK%20Tax%20Credit%20Calculation).pdf""file:///C:/Users/yaoke/OneDrive/Desktop/PolicyEngine/SK/SK%20Tax%20Credit%20Return/I2-01.pdf"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        relative_live_eligibility = person("is_live_together", period)
        is_elderly_dependant = person("is_elderly_dependant", period)
        is_infirm_dependant = person("is_infirm_dependant", period)
        dependants_income = person("dependants_income", period)
        dependant_age = person("dependant_age", period)
    
        p = parameters(period).gov.provinces.sk.tax.income.credits.sk_caregiver_amount

        age_threshold = select([(is_elderly_dependant == 1) & (is_infirm_dependant == 0),
        (is_elderly_dependant == 0) & (is_infirm_dependant == 1),], 
        [p.elderly_age_threshold, p.infirm_age_threshold])
        age_eligibility = where(dependant_age >= age_threshold, 1, 0)
        
        eligibility = relative_live_eligibility & age_eligibility

        return select([eligibility == 0, (eligibility == 1) & (dependants_income >= p.higher_income_threshold), 
        (eligibility == 1) & (dependants_income <= p.lower_income_threshold),
        (eligibility == 1) & (p.higher_income_threshold > dependants_income > p.lower_income_threshold)],
        [0, 0, p.amount, p.higher_income_threshold-dependants_income])