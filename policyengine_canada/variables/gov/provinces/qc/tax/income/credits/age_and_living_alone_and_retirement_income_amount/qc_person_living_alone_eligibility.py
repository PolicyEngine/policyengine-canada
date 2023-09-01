from policyengine_canada.model_api import *


class qc_person_living_alone_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Quebec amount for person living alone eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.age_and_living_alone_and_retirement_income_amount.living_alone_amount

        # if living alone
        living_alone = household("living_alone", period)

        # if not, check cohabitants
        person = household.members
        # under the age of 18
        age_eligible = person("age", period) < p.cohabitant_age_eligibility
        # your children, grandchildren or great-grandchildren 18 or older who were full-time students
        decendant = person("is_decendant", period)
        full_time_student = person("is_full_time_student", period)

        cohabitant_eligible = age_eligible | (decendant & full_time_student)

        return living_alone | household.any(cohabitant_eligible)
