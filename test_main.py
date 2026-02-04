
import subprocess

def run_program():
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    return result.stdout.strip()

def test_greeting():
    output = run_program()
    assert "Hello World" in output, "Expected 'Hello World' in output"
