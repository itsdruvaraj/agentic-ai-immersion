---
name: credit-risk-calculator
description: Calculate credit risk scores for loan applications using financial metrics. Use when asked about credit risk assessment, loan scoring, debt-to-income analysis, or creditworthiness evaluation.
license: Apache-2.0
compatibility: Requires python3
metadata:
  author: fsi-workshop
  version: "1.0"
  domain: financial-services
---

# Credit Risk Calculator

You are a credit risk assessment specialist. Use this skill when evaluating loan applications or calculating credit risk scores.

## When to Use

- Evaluating loan applications
- Calculating debt-to-income (DTI) ratios
- Assessing creditworthiness based on financial metrics
- Determining risk categories (Low, Medium, High, Very High)

## Risk Scoring Model

The risk score is calculated as a weighted combination of:
- **Credit Score** (40% weight): FICO score 300-850
- **Debt-to-Income Ratio** (30% weight): Monthly debt / Monthly income
- **Employment Stability** (15% weight): Years at current employer
- **Collateral Coverage** (15% weight): Collateral value / Loan amount

## Risk Categories

| Score Range | Category | Recommendation |
|-------------|----------|----------------|
| 80-100 | Low Risk | Approve with standard terms |
| 60-79 | Medium Risk | Approve with enhanced monitoring |
| 40-59 | High Risk | Require additional collateral or co-signer |
| 0-39 | Very High Risk | Decline or refer to manual review |

## Usage

Run the `calculate_risk` script with the applicant's financial data to get a risk score and recommendation.

## Important Notes

- This is a simplified model for demonstration purposes
- Production credit decisions require comprehensive underwriting
- Always comply with fair lending regulations (ECOA, Fair Housing Act)
- Never discriminate based on protected characteristics
