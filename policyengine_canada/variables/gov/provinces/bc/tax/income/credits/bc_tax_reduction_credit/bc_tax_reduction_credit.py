from policyengine_canada.model_api import *


class bc_tax_reduction_credit(Variable):
    value_type = float
    entity = Person
    label = "British Columbia tax reduction credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        income = person("bc_taxable_income", period)
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.tax_reduction
        return max_(p.base - p.reduction.calc(income), 0)
