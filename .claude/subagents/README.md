# PolicyEngine Rules PR Reviewer Subagent

## Overview
This subagent specializes in reviewing PolicyEngine pull requests that implement or modify tax and benefit rules. It ensures accuracy against source documents, validates calculations, and checks for completeness.

## Installation
To make this subagent available across all your PolicyEngine repositories:

1. Copy the `.claude/subagents` folder to your home directory or a shared location
2. Set the environment variable: `export CLAUDE_SUBAGENTS_PATH=~/.claude/subagents`
3. The subagent will be automatically available in all Claude sessions

## Usage

### Activating the Subagent
The subagent activates automatically when you:
- Ask to "review a PolicyEngine PR"
- Request to "validate parameters against sources"
- Say "check if this calculation is correct"
- Work with files in `parameters/`, `variables/`, or `tests/` directories

### Example Commands

```
"Review PR #521 that implements EI and CPP payroll taxes"
"Validate the GIS parameters against official government sources"
"Check if the Climate Action Incentive calculation matches the legislation"
"Verify all test cases in this PR by hand calculation"
```

### What It Reviews

#### 1. Parameter Verification
- Checks every parameter value against official sources
- Verifies effective dates match policy implementation
- Validates all reference URLs

#### 2. Calculation Logic
- Steps through formulas to ensure they match legislation
- Checks edge cases and boundary conditions
- Verifies calculations happen at correct entity level

#### 3. Completeness
- Identifies missing eligibility criteria
- Checks for special population handling
- Verifies geographic variations are covered
- Ensures proper time period handling

#### 4. Test Validation
- Manually calculates each test case
- Shows step-by-step work
- Identifies gaps in test coverage
- Suggests additional test scenarios

#### 5. Documentation
- Reviews parameter descriptions
- Checks variable docstrings
- Verifies changelog entries
- Ensures references are complete

## Output Format

The subagent provides a structured review with:

### ✅ Verified Against Sources
Lists all parameters/rules that match official documentation

### ⚠️ Discrepancies Found  
Highlights any differences between PR and source documents

### 🔍 Missing Components
Identifies policy aspects not implemented

### 📊 Test Case Verification
Shows hand calculations for each test with pass/fail status

### 📝 Documentation Issues
Lists missing or unclear documentation

### 💡 Recommendations
Provides actionable suggestions for improvement

### Confidence Level
Rates review confidence (High/Medium/Low) with explanation

## Example Review

```markdown
## PR Review: Implement EI and CPP payroll taxes

### ✅ Verified Against Sources
- EI rate 2024 (0.0166): Matches CRA source
- CPP maximum 2024 ($71,300): Matches official rates
- Basic exemption ($3,500): Correct per legislation

### ⚠️ Discrepancies Found
- CPP2 rate: PR has 0.04, but source shows 0.0400 (formatting)

### 🔍 Missing Components
- Not implemented: Quebec separate QPP system
- Missing: EI fishing benefits special rules

### 📊 Test Case Verification
#### Test: Employee with $50,000 income
**Hand Calculation:**
- Step 1: Pensionable = $50,000 - $3,500 = $46,500
- Step 2: CPP = $46,500 × 0.0595 = $2,766.75
- Result: $2,766.75
- Test expects: $2,766.75
- Status: ✅ Match

### 📝 Documentation Issues
- Missing: Explanation of basic exemption application
- Unclear: How mixed employment/self-employment handled

### 💡 Recommendations
1. Add Quebec QPP as separate parameter tree
2. Include tests for maximum contribution scenarios
3. Document the exemption allocation methodology

### Confidence Level: High
Based on direct verification against CRA T4127 document
```

## Special Features

### Country-Specific Validation

#### Canada
- Checks federal vs provincial jurisdiction
- Verifies Quebec special handling
- Validates both English and French sources

#### United States  
- Validates federal vs state rules
- Checks AMT implications
- Verifies filing status variations

#### United Kingdom
- Checks Scotland/Wales/NI variations
- Validates Universal Credit interactions
- Verifies taper rates

### Red Flags It Catches
- Hardcoded values that should be parameters
- Missing inflation adjustments
- Incorrect period conversions
- Oversimplified phase-outs
- Missing means-testing
- Ignored household composition

## Extending the Subagent

To add new validation rules:

1. Edit `policyengine_rules_reviewer.py`
2. Add new check methods
3. Update the review process
4. Add to configuration in `config.yaml`

## Troubleshooting

If the subagent doesn't activate:
- Check the activation patterns in `config.yaml`
- Ensure file paths match expected patterns
- Verify the subagent is enabled

## Contributing

To improve the subagent:
1. Add new validation patterns
2. Enhance source document parsing
3. Improve calculation verification
4. Add support for more jurisdictions

## License
Same as PolicyEngine repositories (AGPL-3.0)