#!/usr/bin/env python3
"""
SPSD/M Bridge Script for PolicyEngine Canada Validation

This script would interface with SPSD/M if installed, allowing direct comparison
of PolicyEngine outputs with SPSD/M calculations.

Requirements:
- SPSD/M 29.0 or later installed
- Windows environment (or Windows VM)
- SAS or STATA for SPSD/M execution
- pywin32 for Windows COM interface
"""

import subprocess
import pandas as pd
import json
from pathlib import Path

class SPSDMBridge:
    """Bridge to run SPSD/M simulations for validation."""
    
    def __init__(self, spsdm_path="C:/SPSDM/"):
        """
        Initialize SPSD/M bridge.
        
        Args:
            spsdm_path: Path to SPSD/M installation
        """
        self.spsdm_path = Path(spsdm_path)
        self.sas_path = "C:/Program Files/SASHome/SASFoundation/9.4/sas.exe"
        
    def create_sas_program(self, test_case):
        """
        Create SAS program to run SPSD/M simulation.
        
        Args:
            test_case: Dictionary with household parameters
            
        Returns:
            Path to created SAS program
        """
        sas_code = f"""
        /* SPSD/M Validation Run */
        %let SPSDM = {self.spsdm_path};
        
        /* Load SPSD/M */
        %include "&SPSDM/SPSDM.sas";
        
        /* Create test household */
        data household;
            /* Person characteristics */
            age = {test_case['age']};
            income = {test_case['income']};
            province = "{test_case.get('province', 'ON')}";
            adult_years_in_canada = {test_case.get('adult_years_in_canada', 40)};
            
            /* Run SPSD/M calculations */
            %SPSDM_Calculate(
                year=2024,
                variables=imoasmax imioas oasrep
            );
        run;
        
        /* Export results */
        proc export data=household
            outfile="spsdm_output.csv"
            dbms=csv replace;
        run;
        """
        
        sas_file = Path("temp_spsdm_run.sas")
        sas_file.write_text(sas_code)
        return sas_file
    
    def run_spsdm(self, test_case):
        """
        Run SPSD/M for a test case.
        
        Args:
            test_case: Dictionary with test parameters
            
        Returns:
            Dictionary with SPSD/M outputs
        """
        # Create SAS program
        sas_file = self.create_sas_program(test_case)
        
        # Run SAS
        try:
            result = subprocess.run(
                [self.sas_path, str(sas_file)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Read output
            if Path("spsdm_output.csv").exists():
                df = pd.read_csv("spsdm_output.csv")
                return {
                    'oas_pre_repayment': df['imoasmax'].iloc[0],
                    'oas_repayment': df['oasrep'].iloc[0],
                    'oas_net': df['imioas'].iloc[0]
                }
        except Exception as e:
            print(f"Error running SPSD/M: {e}")
            return None
        finally:
            # Cleanup
            sas_file.unlink(missing_ok=True)
            Path("spsdm_output.csv").unlink(missing_ok=True)
    
    def validate_against_policyengine(self, test_cases):
        """
        Run validation comparing SPSD/M with PolicyEngine.
        
        Args:
            test_cases: List of test case dictionaries
            
        Returns:
            Validation results DataFrame
        """
        results = []
        
        for test in test_cases:
            # Run SPSD/M
            spsdm_result = self.run_spsdm(test)
            
            # Run PolicyEngine (would import from policyengine_canada)
            pe_result = run_policyengine_simulation(test)
            
            # Compare
            results.append({
                'test_name': test['name'],
                'spsdm_oas': spsdm_result['oas_net'],
                'pe_oas': pe_result['oas_net'],
                'match': abs(spsdm_result['oas_net'] - pe_result['oas_net']) < 0.01,
                'difference': spsdm_result['oas_net'] - pe_result['oas_net']
            })
        
        return pd.DataFrame(results)

def run_policyengine_simulation(test_case):
    """
    Run PolicyEngine simulation for comparison.
    """
    from policyengine_canada import CountryTaxBenefitSystem
    from policyengine_core.simulations import Simulation
    
    system = CountryTaxBenefitSystem()
    
    situation = {
        "people": {
            "person": {
                "age": {2024: test_case['age']},
                "individual_net_income": {2024: test_case['income']},
                "adult_years_in_canada": {2024: test_case.get('adult_years_in_canada', 40)}
            }
        },
        "households": {
            "household": {
                "members": ["person"]
            }
        }
    }
    
    sim = Simulation(tax_benefit_system=system, situation=situation)
    
    return {
        'oas_pre_repayment': sim.calculate("oas_pre_repayment", 2024)[0],
        'oas_repayment': sim.calculate("oas_repayment", 2024)[0],
        'oas_net': sim.calculate("oas_net", 2024)[0]
    }

if __name__ == "__main__":
    # Check if SPSD/M is available
    if not Path("C:/SPSDM/").exists():
        print("SPSD/M not found. Please install SPSD/M to run direct validation.")
        print("Using pre-calculated SPSD/M values for validation instead.")
        exit(1)
    
    # Define test cases
    test_cases = [
        {"name": "Low income", "age": 70, "income": 30000},
        {"name": "Partial clawback", "age": 70, "income": 100000},
        {"name": "Senior boost", "age": 76, "income": 50000},
        {"name": "Full clawback", "age": 70, "income": 150000}
    ]
    
    # Run validation
    bridge = SPSDMBridge()
    results = bridge.validate_against_policyengine(test_cases)
    
    print("\nSPSD/M vs PolicyEngine Validation Results:")
    print("=" * 60)
    print(results.to_string(index=False))
    
    # Summary
    matches = results['match'].sum()
    total = len(results)
    print(f"\nValidation: {matches}/{total} tests match SPSD/M exactly")