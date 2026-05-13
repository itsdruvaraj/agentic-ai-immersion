"""Credit Risk Calculator Script.

Calculates a risk score based on financial metrics for a loan application.
"""
import json
import sys


def calculate_risk_score(
    credit_score: int,
    annual_income: float,
    monthly_debt: float,
    loan_amount: float,
    employment_years: float,
    collateral_value: float = 0.0,
) -> dict:
    """Calculate credit risk score from financial metrics."""
    # Normalize credit score (300-850 range → 0-100)
    credit_component = max(0, min(100, (credit_score - 300) / 5.5))

    # Debt-to-income ratio (lower is better)
    monthly_income = annual_income / 12
    dti_ratio = monthly_debt / monthly_income if monthly_income > 0 else 1.0
    dti_component = max(0, min(100, (1 - dti_ratio) * 100))

    # Employment stability (capped at 10 years)
    employment_component = min(100, (employment_years / 10) * 100)

    # Collateral coverage ratio
    collateral_ratio = collateral_value / loan_amount if loan_amount > 0 else 0
    collateral_component = min(100, collateral_ratio * 100)

    # Weighted score
    risk_score = (
        credit_component * 0.40
        + dti_component * 0.30
        + employment_component * 0.15
        + collateral_component * 0.15
    )

    # Determine category
    if risk_score >= 80:
        category = "Low Risk"
        recommendation = "Approve with standard terms"
    elif risk_score >= 60:
        category = "Medium Risk"
        recommendation = "Approve with enhanced monitoring"
    elif risk_score >= 40:
        category = "High Risk"
        recommendation = "Require additional collateral or co-signer"
    else:
        category = "Very High Risk"
        recommendation = "Decline or refer to manual review"

    return {
        "risk_score": round(risk_score, 1),
        "category": category,
        "recommendation": recommendation,
        "details": {
            "credit_component": round(credit_component, 1),
            "dti_component": round(dti_component, 1),
            "dti_ratio": round(dti_ratio, 3),
            "employment_component": round(employment_component, 1),
            "collateral_component": round(collateral_component, 1),
        },
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calculate credit risk score")
    parser.add_argument("--credit_score", type=int, required=True)
    parser.add_argument("--annual_income", type=float, required=True)
    parser.add_argument("--monthly_debt", type=float, required=True)
    parser.add_argument("--loan_amount", type=float, required=True)
    parser.add_argument("--employment_years", type=float, required=True)
    parser.add_argument("--collateral_value", type=float, default=0.0)

    args = parser.parse_args()
    result = calculate_risk_score(
        credit_score=args.credit_score,
        annual_income=args.annual_income,
        monthly_debt=args.monthly_debt,
        loan_amount=args.loan_amount,
        employment_years=args.employment_years,
        collateral_value=args.collateral_value,
    )
    print(json.dumps(result, indent=2))
