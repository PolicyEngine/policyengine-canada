from policyengine_canada.model_api import *


class yt_childrens_fitness_tax_credit_disability_supplement(Variable):
    value_type = float
    entity = Household
    label = "Yukon children fitness tax credit disability supplement"
    definition_period = YEAR
    unit = CAD
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        disabled_children = household("yt_cftc_disabled_children", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_fitness.disability_supplement
        return disabled_children * p.base
