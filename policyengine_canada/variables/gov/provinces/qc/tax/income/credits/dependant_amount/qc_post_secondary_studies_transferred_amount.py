from policyengine_canada.model_api import *


class qc_post_secondary_studies_transferred_amount(Variable):
    value_type = float
    entity = Person
    label = "Quebec amount transferred by a child enrolled in post-secondary studies"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.depedant_amount

        # Child over 18 enrolled in post-secondary studies
        age_eligible = person("age", period) < p.age_eligibility
        full_time_student = person("is_full_time_student", period)
        eligible = age_eligible & full_time_student

        # Amount that you can transfer
        base_amount = p.post_secondary_studies_transferred_amount
        post_secondary_studies_amount = person(
            "qc_post_secondary_studies_amount", period
        )

        # TODO: REDUCTION line 8-16
        # https://www.revenuquebec.ca/documents/en/formulaires/tp/2022-12/TP-1.D.S-V%282022-12%29.pdf
