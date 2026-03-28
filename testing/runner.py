import subprocess

def run_tests():
    try:
        completed = subprocess.run(
            ["pytest", "test_generated.py", "-q"],
            capture_output=True,
            text=True
        )

        success = completed.returncode == 0

        return {
            "success": success,
            "output": completed.stdout + completed.stderr
        }

    except Exception as e:
        return {
            "success": False,
            "output": str(e)
        }