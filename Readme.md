                                                                                AI Code Analyzer CLI

                            

Analyzes AI-generated code for logical issues, generates tests,
and evaluates test quality using mutation testing.



⚡ Features
Static code analysis (AST-based)
Rule-based bug detection
Automatic test generation
Parallel mutation testing
Confidence scoring



🛠️ Tech Stack
Python
AST parsing
Pytest
Concurrent Futures (parallelism)




▶️ How to run
git clone ai-code-analyzer-cli
cd ai-code-analyzer-cli
pip install -r requirements.txt
python main.py analyze big_sample.py




📊 Sample Output

📍 Function: transfer_money
⚠️ Issues:
 - No balance validation before deduction

🧪 Tests: ✅ Passed
🧬 Mutation Score: 40.00%
📊 Confidence: MEDIUM




🎯 Why this project
AI-generated code often works locally but breaks at scale.
This tool adds a testing + validation layer to improve reliability.