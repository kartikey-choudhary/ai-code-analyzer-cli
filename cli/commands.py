from analyzer.ast_parser import extract_functions
from analyzer.rule_engine import analyze_rules
from testing.test_generator import generate_tests
from testing.runner import run_tests
from mutation.mutator import run_mutations


def analyze_code(file_path):
    open("test_generated.py", "w").close()
    results = []

    functions = extract_functions(file_path)

    for func in functions:
        issues = analyze_rules(func)

        results.append({
            "name": func["name"],
            "issues": issues
        })

        module_name = file_path.replace(".py", "")
        test_code = generate_tests(func, module_name)

        with open("test_generated.py", "a") as f:
            f.write("\n\n" + test_code)

    print("\n🧪 Running tests...")
    test_result = run_tests()

    # 🔥 FIX: Only run mutation if tests pass
    if test_result["success"]:
        print("\n🧬 Running mutation testing...")
        score = run_mutations(file_path)
    else:
        print("\n⚠️ Skipping mutation testing (tests failed)")
        score = 0.0

    print("\n" + "=" * 40)
    print(f"📂 File: {file_path}")

    for res in results:
        print("\n📍 Function:", res["name"])

        if res["issues"]:
            print("⚠️ Issues:")
            for issue in res["issues"]:
                print(f" - {issue}")
        else:
            print("✅ No issues")

    # Test summary
    if test_result["success"]:
        print("\n🧪 Tests: ✅ Passed")
    else:
        print("\n🧪 Tests: ❌ Failed")

    # Mutation summary
    if test_result["success"]:
        print(f"🧬 Mutation Score: {score:.2f}%")

        if score > 80:
            print("📊 Confidence: HIGH")
        elif score > 50:
            print("📊 Confidence: MEDIUM")
        else:
            print("📊 Confidence: LOW")
    else:
        print("🧬 Mutation Score: N/A (tests failed)")
        print("📊 Confidence: LOW")

    print("=" * 40)