from policyengine_canada.model_api import *


class yt_tax_taxable_income(Variable):
    value_type = float
    entity = Person
    label = "Yukon income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-22e.pdf"
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        income = person("yt_taxable_income", period)
        p = parameters(period).gov.provinces.yt.tax.income.rate
        return p.calc(income)
