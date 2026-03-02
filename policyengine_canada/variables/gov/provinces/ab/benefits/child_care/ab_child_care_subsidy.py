from policyengine_canada.model_api import *


class ab_child_care_subsidy(Variable):
    value_type = float
    entity = Household
    label = "Alberta Child Care Subsidy"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB
    reference = "https://www.alberta.ca/child-care-subsidy"

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.ab.benefits.child_care
        income = household("adjusted_family_net_income", period)

        person = household.members
        age = person("age", period)

        # Per alberta.ca, subsidy depends on child age group
        preschool_age = p.age_threshold.preschool
        school_age_max = p.age_threshold.school_age_max

        is_preschool = age < preschool_age
        is_school_age = (age >= preschool_age) & (age <= school_age_max)

        # Look up monthly subsidy from income bracket tables
        preschool_monthly = p.subsidy_schedule.preschool.calc(income)
        school_age_monthly = p.subsidy_schedule.school_age.calc(income)

        monthly_subsidy = where(
            is_preschool,
            preschool_monthly,
            where(is_school_age, school_age_monthly, 0),
        )

        # Annual subsidy = monthly amount * 12 months
        annual_per_child = monthly_subsidy * 12

        return household.sum(annual_per_child)
