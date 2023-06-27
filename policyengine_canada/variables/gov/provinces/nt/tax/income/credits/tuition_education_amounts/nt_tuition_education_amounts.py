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
        
        tuition = person('tuition_expenses', period)
        eligible = tuition > p.base_tuition_amount

        full_time_amount = person('is_full_time_student', period) * p.full_time_amount + person('is_part_time_student', period) * person('is_disabled', period) * p.full_time_amount
        part_time_amount = person('is_part_time_student', period) * (~person('is_disabled', period)) * p.part_time_amount

        tuition_education_amounts = tuition + (full_time_amount + part_time_amount) * 12

        return eligible * tuition_education_amounts