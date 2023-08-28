from policyengine_canada.model_api import *


class ns_income_assistance_applicable_assets(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia income assistance applicable assets"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
    defined_for = ProvinceCode.NS

    adds = "gov.provinces.ns.tax.income.income_assistance.eligibility.assets.applicable_assets"

    # None of the following is an applicable asset:
    # the home of an applicant or recipient, if the property is located in the Province and is assessed at less than twice
    # the average assessed value of single-family dwellings in the municipality where it is located;
    # a cash surrender value of under $500 of a life insurance policy;
    # a motor vehicle used for basic transportation including transportation related to employment search requirements,
    # training or health and safety requirements;
    # tools or equipment directly related to a trade or profession;
    # a registered education savings plan established for the education of a child and intended for use by that
    # child in relation to education expenses;
    # a registered disability savings plan;
    # any portion of a registered retirement savings plan that is
    # part of an employment pension program at the place of employment where the applicant or recipient is employed,
    # temporarily laid off or on sick leave, or
    # part or all of a locked-in retirement account as defined by the Pension Benefits Regulations made under
    # the Pension Benefits Act;
    # prepaid funeral arrangements up to a maximum value of $5000;
    # funds saved from participating in a savings program that is designed to promote self-sufficiency
    #  and is approved by the Minister.
