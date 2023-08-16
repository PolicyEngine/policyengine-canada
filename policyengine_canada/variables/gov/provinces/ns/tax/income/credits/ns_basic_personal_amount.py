from policyengine_canada.model_api import *


class ns_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Basic Personal Amount"
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    reference = (
        "https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf#page=1",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5003-d/5003-d-22e.pdf#page=1",
        "https://nslegislature.ca/sites/default/files/legc/statutes/income%20tax.pdf#page=24",
    )

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.basic_personal_amount
        taxable_income = person("total_individual_pre_tax_income", period)

        # Calculate additional amount added to base amount
        exceedance = max_(
            taxable_income - p.additional_amount.income_threshold, 0
        )
        reduced_additional_amount = (
            p.additional_amount.additional_amount
            - p.additional_amount.applicable_rate * exceedance
        )
        additional_amount = max_(0, reduced_additional_amount)
        additional_amount = min_(
            additional_amount, p.additional_amount.additional_amount
        )

        return p.base + additional_amount