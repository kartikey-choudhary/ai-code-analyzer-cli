import requests


# ✅ FAST MODEL (Gemma)
def gemma_fix(code, issues):
    prompt = f"""
You are a senior backend engineer.

Fix the following Python function:

{code}

Issues:
{issues}

STRICT RULES:
- DO NOT use print statements
- Use proper exceptions
- DO NOT change function signature
- Add validation and error handling

Return ONLY corrected code.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    if "response" in data:
        return data["response"]
    elif "message" in data:
        return data["message"]["content"]

    return str(data)


# ✅ ACCURATE MODEL (DeepSeek fallback)
def deepseek_fix(code, issues):
    prompt = f"""
Fix this Python function properly:

{code}

Issues:
{issues}

Return only corrected code.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "deepseek-r1:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    if "response" in data:
        return data["response"]
    elif "message" in data:
        return data["message"]["content"]

    return str(data)


# ✅ CHECK IF OUTPUT IS GOOD
def is_good_fix(output, issues):
    if not output:
        return False

    # if issues exist, we expect proper handling
    if issues:
        if "raise" not in output:
            return False

    # reject bad patterns
    if "print(" in output:
        return False

    return True


# ✅ MAIN FUNCTION (THIS IS USED BY CLI)
def generate_ai_fix(code, issues):
    # print("\n⚡ Trying fast model (Gemma)...")
    # fast_output = gemma_fix(code, issues)

    # if is_good_fix(fast_output, issues):
    #     print("✅ Fast model success")
    #     return fast_output

    # print("⚠️ Falling back to DeepSeek...")
    # return deepseek_fix(code, issues)
    return "⚠️ AI suggestions disabled in prototype. Review issues manually."