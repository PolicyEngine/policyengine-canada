from policyengine_canada.model_api import *


class qc_children_activities_credit_eligible(Variable):
    value_type = bool
    entity = Household
    label = (
        "Eligible for the Quebec children's activities tax credit household"
    )
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        return (
            household("adjusted_family_net_income", period) <= p.income_limit
        )
