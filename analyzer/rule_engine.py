def analyze_rules(func):
    issues = []
    code = func["source"]

    # Generic checks
    if "if" not in code:
        issues.append("No conditional checks found (possible missing validation)")

    if "try" not in code:
        issues.append("No error handling detected")

    # 🔥 Specific rules

    if "/" in code:
        issues.append("Possible division by zero risk")

    if "password" in code and "==" in code:
        issues.append("Hardcoded credential check detected (security risk)")

    if "balance" in code and "-" in code:
        issues.append("No balance validation before deduction")

    if "amount" in code and "<=" not in code:
        issues.append("Amount not validated (could be negative or zero)")

    return issues