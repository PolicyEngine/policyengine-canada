from policyengine_canada.model_api import *


class ns_age_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Age tax credit"
    definition_period = YEAR
    defined_for = "ns_age_amount_supplement_eligible"
    reference = (
        "https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ns-ws/td1ns-ws-23e.pdf#page=1",
        "https://nslegislature.ca/sites/default/files/legc/statutes/income%20tax.pdf#page=28",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        income = person("ns_taxable_income", period)
        p = parameters(period).gov.provinces.ns.tax.income.credits.age
        eligibility = (income < p.income_eligibility)

        return eligibility * p.amount
