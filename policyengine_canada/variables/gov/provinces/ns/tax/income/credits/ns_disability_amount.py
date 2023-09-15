from policyengine_canada.model_api import *


class ns_disability_amount(Variable):
    value_type = bool
    entity = Person
    label = "Nova Scotia Disability Amount"
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    reference = "https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf#page=1"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.disability_amount
        isdisabled = person("person_disability_situation", period)
        disability_amount = p.amount

        return where(isdisabled, disability_amount, 0)
