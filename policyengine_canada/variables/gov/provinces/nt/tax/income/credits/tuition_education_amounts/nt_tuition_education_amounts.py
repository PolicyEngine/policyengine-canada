from policyengine_canada.model_api import *


class nt_tuition_education_amounts(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Tuition and Education Amounts "
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.tuition_education_amounts

        tuition = person("tuition_expenses", period)
        months = person("number_of_months_student", period)
        eligible = tuition > p.base_tuition_amount
        taxable_income = person("nt_income_tax_before_credits", period)

        full_time_amount = (
            person("is_full_time_student", period) * p.full_time_amount
            + person("is_part_time_student", period)
            * person("is_disabled", period)
            * p.full_time_amount
        )
        part_time_amount = (
            person("is_part_time_student", period)
            * (~person("is_disabled", period))
            * p.part_time_amount
        )

        tuition_education_amounts = (tuition + (full_time_amount + part_time_amount) * months)

        total_available_tuition_education_amounts = eligible * tuition_education_amounts

        adjusted_taxable_income = (
            taxable_income
            if taxable_income <= p.reduction.income_threshold
            else (p.reduction.income_threshold / p.reduction.rate - p.reduction.income_threshold))

        return (
            min_(
                total_available_tuition_education_amounts,
                adjusted_taxable_income,
            )
            + adjusted_taxable_income
        )
