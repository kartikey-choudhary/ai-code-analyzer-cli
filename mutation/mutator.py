from concurrent.futures import ThreadPoolExecutor
from testing.runner import run_tests


def mutate_code(code):
    mutants = []

    replacements = [
        ("+", "-"),
        ("-", "+"),
        ("*", "/"),
        ("/", "*"),
        ("==", "!="),
        ("!=", "=="),
        (">", "<"),
        ("<", ">"),
    ]

    for old, new in replacements:
        if old in code:
            mutated = code.replace(old, new, 1)
            mutants.append(mutated)

    return mutants


def test_mutant(mutant_code, file_path):
    try:
        with open(file_path, "w") as f:
            f.write(mutant_code)

        result = run_tests()

        return not result["success"]  # True = killed

    except:
        return True


def run_mutations(file_path):
    print("🧬 Running mutation testing...")

    with open(file_path, "r") as f:
        original_code = f.read()

    mutants = mutate_code(original_code)

    if not mutants:
        print("⚠️ No mutants generated.")
        return 0.0

    print(f"💡 {len(mutants)} mutants generated, running in parallel...")

    results = []

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(test_mutant, m, file_path)
            for m in mutants
        ]

        for future in futures:
            results.append(future.result())

    # restore original file
    with open(file_path, "w") as f:
        f.write(original_code)

    killed = sum(results)
    survived = len(mutants) - killed

    print(f"💀 Killed mutants: {killed}")
    print(f"🧬 Survived mutants: {survived}")

    score = (killed / len(mutants)) * 100
    return score