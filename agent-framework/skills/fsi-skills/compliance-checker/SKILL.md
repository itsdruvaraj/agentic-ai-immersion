---
name: compliance-checker
description: Check financial transactions and operations against regulatory compliance rules. Use when asked about AML screening, KYC verification, transaction monitoring, or regulatory compliance.
license: Apache-2.0
compatibility: Requires python3
metadata:
  author: fsi-workshop
  version: "1.0"
  domain: financial-services
---

# Compliance Checker

You are a financial compliance specialist. Use this skill when checking transactions or operations against regulatory rules.

## When to Use

- Screening transactions for Anti-Money Laundering (AML) red flags
- Verifying Know Your Customer (KYC) requirements
- Checking transaction limits and patterns
- Identifying suspicious activity indicators

## Compliance Rules

### Transaction Monitoring Thresholds

| Rule | Threshold | Action |
|------|-----------|--------|
| Large Cash Transaction | > $10,000 | File CTR (Currency Transaction Report) |
| Structuring Detection | Multiple transactions just under $10,000 | Flag for SAR review |
| Wire Transfer Reporting | International > $3,000 | Record and verify |
| High-Risk Country | FATF grey/black list | Enhanced Due Diligence |

### KYC Verification Levels

- **Basic**: Name, address, date of birth, ID document
- **Enhanced**: Source of funds, purpose of account, beneficial ownership
- **Ongoing**: Transaction monitoring, periodic review, PEP screening

## Red Flag Indicators

1. Rapid movement of funds across multiple accounts
2. Transactions inconsistent with stated business purpose
3. Use of shell companies or nominees
4. Reluctance to provide identification
5. Transactions just below reporting thresholds (structuring)

## Important Disclaimers

- This is a simplified compliance framework for demonstration
- Real compliance requires certified AML/KYC systems
- Always escalate suspicious activity to compliance officers
- Follow your institution's BSA/AML program requirements
