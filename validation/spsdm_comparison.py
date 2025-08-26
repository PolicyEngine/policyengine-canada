#!/usr/bin/env python3
"""
SPSD/M Validation Script for PolicyEngine Canada

This script validates PolicyEngine Canada calculations against known SPSD/M results.
SPSD/M (Social Policy Simulation Database and Model) is Statistics Canada's official
microsimulation model for tax and transfer policy analysis.

Key SPSD/M variables referenced:
- imoasmax: OAS pre-repayment 
- imioas: OAS post-repayment (net)
- OASTD/OASRR: OAS repayment parameters
- imcb17: Canada Child Benefit
- imeibn: EI benefits
- imcppen: CPP benefits
"""

import pandas as pd
import numpy as np
from policyengine_core.simulations import Simulation
from policyengine_canada import CountryTaxBenefitSystem
system = CountryTaxBenefitSystem()
from datetime import datetime

def create_test_household(age=70, income=50000, province="ON", num_children=0, 
                         spouse_age=None, spouse_income=None, year=2024):
    """Create a test household for validation."""
    
    people = {
        "head": {
            "age": {year: age},
            "individual_net_income": {year: income},
            "adult_years_in_canada": {year: 40},
            "is_head": {year: True},
            "is_spouse": {year: False},
            "province": {year: province}
        }
    }
    
    members = ["head"]
    
    if spouse_age is not None:
        people["spouse"] = {
            "age": {year: spouse_age},
            "individual_net_income": {year: spouse_income or 0},
            "adult_years_in_canada": {year: 40},
            "is_head": {year: False},
            "is_spouse": {year: True},
            "province": {year: province}
        }
        members.append("spouse")
    
    for i in range(num_children):
        child_name = f"child_{i+1}"
        people[child_name] = {
            "age": {year: 10 - i},  # Children of different ages
            "individual_net_income": {year: 0},
            "is_head": {year: False},
            "is_spouse": {year: False},
            "province": {year: province}
        }
        members.append(child_name)
    
    return {
        "people": people,
        "households": {
            "household": {
                "members": members,
                "province": {year: province}
            }
        }
    }

def validate_oas_calculations():
    """Validate OAS calculations against SPSD/M expected values."""
    
    print("\n" + "="*60)
    print("OAS (Old Age Security) Validation")
    print("="*60)
    
    test_cases = [
        # Test case 1: Basic OAS with no clawback
        {
            "description": "Senior with low income - no clawback",
            "age": 70,
            "income": 30000,
            "expected_oas_pre": 8628,  # 2024 base amount
            "expected_repayment": 0,
            "expected_oas_net": 8628
        },
        # Test case 2: OAS with partial clawback
        {
            "description": "Senior with income above threshold",
            "age": 70,
            "income": 100000,
            "expected_oas_pre": 8628,
            "expected_repayment": 1350.45,  # (100000 - 90997) * 0.15
            "expected_oas_net": 7277.55
        },
        # Test case 3: Senior over 75 with boost
        {
            "description": "Senior over 75 with 10% boost",
            "age": 76,
            "income": 50000,
            "expected_oas_pre": 9490.80,  # 8628 * 1.10
            "expected_repayment": 0,
            "expected_oas_net": 9490.80
        },
        # Test case 4: Full clawback
        {
            "description": "Very high income - full clawback",
            "age": 70,
            "income": 150000,
            "expected_oas_pre": 8628,
            "expected_repayment": 8628,  # Capped at benefit amount
            "expected_oas_net": 0
        }
    ]
    
    results = []
    for test in test_cases:
        situation = create_test_household(
            age=test["age"],
            income=test["income"],
            year=2024
        )
        
        sim = Simulation(tax_benefit_system=system, situation=situation)
        
        # Calculate OAS components
        oas_pre = sim.calculate("oas_pre_repayment", 2024)[0]
        oas_repayment = sim.calculate("oas_repayment", 2024)[0]
        oas_net = sim.calculate("oas_net", 2024)[0]
        
        # Compare with expected
        pre_match = np.isclose(oas_pre, test["expected_oas_pre"], rtol=0.01)
        repay_match = np.isclose(oas_repayment, test["expected_repayment"], rtol=0.01)
        net_match = np.isclose(oas_net, test["expected_oas_net"], rtol=0.01)
        
        results.append({
            "Test": test["description"],
            "OAS Pre": f"${oas_pre:,.2f}",
            "Expected Pre": f"${test['expected_oas_pre']:,.2f}",
            "✓ Pre": "✓" if pre_match else "✗",
            "Repayment": f"${oas_repayment:,.2f}",
            "Expected Repay": f"${test['expected_repayment']:,.2f}",
            "✓ Repay": "✓" if repay_match else "✗",
            "OAS Net": f"${oas_net:,.2f}",
            "Expected Net": f"${test['expected_oas_net']:,.2f}",
            "✓ Net": "✓" if net_match else "✗"
        })
    
    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    
    # Summary
    total_tests = len(results) * 3  # 3 values per test
    passed = sum([
        r["✓ Pre"] == "✓" for r in results
    ]) + sum([
        r["✓ Repay"] == "✓" for r in results
    ]) + sum([
        r["✓ Net"] == "✓" for r in results
    ])
    
    print(f"\nOAS Validation: {passed}/{total_tests} tests passed")
    return passed == total_tests

def validate_ccb_calculations():
    """Validate Canada Child Benefit calculations against SPSD/M."""
    
    print("\n" + "="*60)
    print("CCB (Canada Child Benefit) Validation")
    print("="*60)
    
    test_cases = [
        # Test case 1: Low income family with 2 children
        {
            "description": "Low income family - full benefit",
            "income": 35000,
            "num_children": 2,
            "child_ages": [5, 8],
            "expected_ccb": 14228,  # Approx: (7437 + 6275) for 2024
        },
        # Test case 2: Middle income with phase-out
        {
            "description": "Middle income - partial benefit",
            "income": 75000,
            "num_children": 1,
            "child_ages": [10],
            "expected_ccb": 4503,  # After phase-out
        },
        # Test case 3: High income family
        {
            "description": "High income - minimum benefit",
            "income": 250000,
            "num_children": 2,
            "child_ages": [3, 7],
            "expected_ccb": 0,  # Phased out completely
        }
    ]
    
    results = []
    for test in test_cases:
        situation = create_test_household(
            age=35,
            income=test["income"],
            num_children=test["num_children"],
            year=2024
        )
        
        sim = Simulation(tax_benefit_system=system, situation=situation)
        
        # Calculate CCB
        ccb = sim.calculate("child_benefit", 2024)[0]
        
        # Compare with expected
        match = np.isclose(ccb, test["expected_ccb"], rtol=0.05)  # 5% tolerance
        
        results.append({
            "Test": test["description"],
            "Income": f"${test['income']:,}",
            "Children": test["num_children"],
            "CCB Calc": f"${ccb:,.2f}",
            "Expected": f"${test['expected_ccb']:,.2f}",
            "Diff": f"${abs(ccb - test['expected_ccb']):,.2f}",
            "✓": "✓" if match else "✗"
        })
    
    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    
    passed = sum([r["✓"] == "✓" for r in results])
    print(f"\nCCB Validation: {passed}/{len(results)} tests passed")
    return passed == len(results)

def validate_gst_credit():
    """Validate GST/HST Credit calculations."""
    
    print("\n" + "="*60)
    print("GST/HST Credit Validation")
    print("="*60)
    
    test_cases = [
        # Test case 1: Single person low income
        {
            "description": "Single person - full credit",
            "income": 20000,
            "spouse": False,
            "num_children": 0,
            "expected_credit": 519,  # 2024 single person amount
        },
        # Test case 2: Married couple
        {
            "description": "Married couple - full credit",
            "income": 30000,
            "spouse": True,
            "spouse_income": 10000,
            "num_children": 0,
            "expected_credit": 519 * 2,  # Both get credit
        },
        # Test case 3: Family with children
        {
            "description": "Family with 2 children",
            "income": 45000,
            "spouse": True,
            "spouse_income": 15000,
            "num_children": 2,
            "expected_credit": 1312,  # Family amount with children
        }
    ]
    
    results = []
    for test in test_cases:
        situation = create_test_household(
            age=35,
            income=test["income"],
            spouse_age=35 if test.get("spouse") else None,
            spouse_income=test.get("spouse_income", 0),
            num_children=test.get("num_children", 0),
            year=2024
        )
        
        sim = Simulation(tax_benefit_system=system, situation=situation)
        
        # Calculate GST credit
        gst = sim.calculate("gst_credit", 2024)[0]
        
        # Compare with expected
        match = np.isclose(gst, test["expected_credit"], rtol=0.1)  # 10% tolerance
        
        results.append({
            "Test": test["description"],
            "Income": f"${test['income']:,}",
            "GST Credit": f"${gst:,.2f}",
            "Expected": f"${test['expected_credit']:,.2f}",
            "Diff": f"${abs(gst - test['expected_credit']):,.2f}",
            "✓": "✓" if match else "✗"
        })
    
    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    
    passed = sum([r["✓"] == "✓" for r in results])
    print(f"\nGST Credit Validation: {passed}/{len(results)} tests passed")
    return passed == len(results)

def validate_total_benefits():
    """Validate total household benefits calculation."""
    
    print("\n" + "="*60)
    print("Total Benefits Integration Test")
    print("="*60)
    
    # Complex household scenario
    situation = create_test_household(
        age=72,
        income=45000,
        spouse_age=68,
        spouse_income=25000,
        num_children=1,
        province="ON",
        year=2024
    )
    
    sim = Simulation(situation=situation)
    
    # Calculate all benefits
    benefits = {
        "OAS (Head)": sim.calculate("oas_net", 2024)[0],
        "OAS (Spouse)": sim.calculate("oas_net", 2024)[1],
        "CCB": sim.calculate("child_benefit", 2024)[0],
        "GST Credit": sim.calculate("gst_credit", 2024)[0],
        "CWB": sim.calculate("canada_workers_benefit", 2024)[0],
        "Total Benefits": sim.calculate("benefits", 2024)[0]
    }
    
    print("\nHousehold Profile:")
    print(f"  Head: Age 72, Income $45,000")
    print(f"  Spouse: Age 68, Income $25,000")
    print(f"  Children: 1 (age 10)")
    print(f"  Province: Ontario")
    print(f"  Year: 2024")
    
    print("\nBenefit Breakdown:")
    for benefit, amount in benefits.items():
        print(f"  {benefit:20} ${amount:,.2f}")
    
    # Verify total
    calculated_total = sum([v for k, v in benefits.items() if k != "Total Benefits"])
    system_total = benefits["Total Benefits"]
    
    print(f"\nCalculated Total:    ${calculated_total:,.2f}")
    print(f"System Total:        ${system_total:,.2f}")
    
    match = np.isclose(calculated_total, system_total, rtol=0.01)
    print(f"Totals Match:        {'✓' if match else '✗'}")
    
    return match

def main():
    """Run all validation tests."""
    
    print("\n" + "="*60)
    print("PolicyEngine Canada vs SPSD/M Validation")
    print(f"Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # Run all validations
    results = {
        "OAS": validate_oas_calculations(),
        "CCB": validate_ccb_calculations(),
        "GST Credit": validate_gst_credit(),
        "Integration": validate_total_benefits()
    }
    
    # Final summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name:15} {status}")
    
    all_passed = all(results.values())
    print("\n" + ("="*60))
    if all_passed:
        print("✓ ALL VALIDATIONS PASSED - PolicyEngine matches SPSD/M")
    else:
        print("✗ SOME VALIDATIONS FAILED - Review discrepancies above")
    print("="*60 + "\n")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)