from policyengine_canada.model_api import *

class nb_tuition_amount(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick tuition amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-s11/5004-s11-22e.pdf"
    defined_for = ProvinceCode.NB

    def formula(person, period, parameters):
        income = person("nb_taxable_income", period)
        p = parameters(period).gov.provinces.nb.tax.income.rate
        return p.calc(income)
