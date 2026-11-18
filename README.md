# Game Glitch Investigator Pro: Agentic AI Strategy & Reliability Suite

## Project Overview & Base Project
This project extends the **Game Glitch Investigator** (from CodePath AI110 Module 1) into a complete applied AI system. The original base project was a Streamlit number-guessing game that suffered from inverted hint feedback, unvalidated user inputs, and unhandled runtime crashes. This upgraded version introduces an **Agentic AI Strategy Coach with RAG-lite context retrieval**, input validation guardrails, and modular state management to deliver reliable gameplay.

---

## Architecture Overview
The system architecture (`diagrams/architecture.mmd`) is organized into three layers:
1. **User and Interface Layer:** Captures raw string inputs through Streamlit widgets and manages reactive session state across script reruns.
2. **Core AI and Logic System:** Routes input through a defensive type/range guardrail (`parse_guess`), queries the **Agentic AI Coach & RAG Retriever** to retrieve distance-based strategy rules, and determines game outcomes via `check_guess`.
3. **Reliability and Verification Layer:** Combines human-in-the-loop testing with automated `pytest` verification to check edge cases and agent responses.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/suhanapatodi/applied-ai-system-final.git](https://github.com/suhanapatodi/applied-ai-system-final.git)
   cd applied-ai-system-final
Create and Activate a Virtual Environment:

Bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate.ps1
Install Dependencies:

Bash
python -m pip install --upgrade pip
pip install -r requirements.txt
Run the Application:

Bash
streamlit run app.py
Sample Interactions
Example 1: Winning Guess & AI Coach Confirmation
Input: User enters 50 on Normal difficulty when the secret number is 50.

AI Output:

Plaintext
🤖 AI Strategy Coach: AI Coach: Target acquired! Optimal solution reached. (Confidence: 1.0)
Win: Congratulations! You guessed the correct number! Total attempts: 1
Example 2: Out-of-Bounds Input Guardrail
Input: User enters 150 on Normal difficulty (valid range: 1–100).

AI Output:

Plaintext
Guess must be between 1 and 100.
Example 3: Dynamic RAG-Lite Strategy Guidance
Input: User guesses 20 on Normal difficulty when the secret number is 50.

AI Output:

Plaintext
🤖 AI Strategy Coach: AI Coach Analysis: 20 was too low. Strategy Rule: You are far off. Consider utilizing a binary search midpoint strategy to cut the search space in half. (Confidence: 0.95)
Design Decisions & Trade-offs
Modular Logic Separation: Isolating the AI strategy coach, input parser, and game rules inside logic_utils.py (separate from app.py) allowed direct unit testing without launching the Streamlit UI.

Defensive Return Tuples: Returning explicit (ok, value, error) tuples from parse_guess instead of raising raw exceptions prevents UI crashes when users submit empty strings or non-numeric text, at the trade-off of slightly more verbose conditional checks in app.py.

Testing Summary
What Worked: Separating core logic made automated testing straightforward, and defensive guardrails caught empty strings, non-numeric inputs, and out-of-bounds numbers reliably.

What Didn't: Initial testing revealed that float strings like "50.0" failed direct int() conversion, requiring an explicit float-to-integer parsing fallback.

What I Learned: Reliable AI features depend heavily on deterministic input validation and clear state separation before any reasoning or hint generation happens.

Reflection
Working on this project showed me that building an applied AI system is less about adding complex features and more about making sure every layer handles unexpected inputs safely. Combining structured guardrails with dynamic strategy retrieval taught me how to keep AI behavior predictable and easy to debug. 


---

### Commit & Push Part 3
Save `README.md` (`Cmd + S`) and run:

```bash
git add README.md
git commit -m "docs: complete Part 3 README documentation"
git push origin main
