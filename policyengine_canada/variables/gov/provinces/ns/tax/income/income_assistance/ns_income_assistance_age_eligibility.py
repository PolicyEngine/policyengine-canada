from policyengine_canada.model_api import *


class ns_income_assistance_age_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Nova Scotia income assistance age eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility
        dependant = person("is_dependant", period)
        protective_services = person("in_need_of_protective_services", period)
        # Person is eligible if over 19 years of age
        age_eligible = age >= p.age_eligibility
        # Person is ineligible if they are a dependant at 21 or older
        dependant_ineligible = (age >= p.dependant_age_eligibility) & (
            dependant == True
        )
        # Person is eligible if between 16 and 19, and is in need of protective services
        protective_services_age_eligible = (
            p.lower_age_eligibility <= age & age < p.age_eligibility
        )
        protective_services_eligible = (
            protective_services * protective_services_age_eligible
        )
        return where(
            dependant_ineligible,
            0,
            (age_eligible | protective_services_eligible),
        )
