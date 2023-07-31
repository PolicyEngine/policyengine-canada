from policyengine_canada.model_api import *


class ns_basic_personal_credits(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Basic Personal Amount"
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    reference = ("https://hr.acadiau.ca/files/sites/hr/Payroll/Pensions%20&%20Benefits/NS_TD1_2022.pdf", 
                 "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5003-d/5003-d-22e.pdf")

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.ns_basic_personal_amount
        taxable_income = person("total_individual_pre_tax_income", period)
        
        # Income Condition
        lower_income_condition = (taxable_income <= p.lower_income_threshold)
        medium_income_condition = (p.lower_income_threshold
                                    < taxable_income
                                    < p.higher_income_threshold)
        higher_income_condition = (taxable_income >= p.higher_income_threshold)

        # Basic Personal Amount
        lower_basic_personal_amount = p.additional_amount + p.basic_amount
        medium_basic_personal_amount = p.basic_amount + 3000 - p.applicable_rate * (taxable_income - p.lower_income_threshold)
        higher_basic_personal_amount = p.basic_amount



        return select(
            [
                lower_income_condition,
                medium_income_condition,
                higher_income_condition,
            ],
            [
                lower_basic_personal_amount,
                medium_basic_personal_amount,
                higher_basic_personal_amount,
            ],
        )
