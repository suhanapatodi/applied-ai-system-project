# Model Card & Responsible AI Reflection

## System Overview
- **System Name:** Game Glitch Investigator Pro: Agentic AI Strategy & Reliability Suite
- **Base Project:** Game Glitch Investigator (CodePath AI110 Module 1)
- **Core Purpose:** Combines number-guessing gameplay with an Agentic AI Strategy Coach, RAG-lite context retrieval, robust input guardrails, and automated reliability evaluation.

---

## 1. Limitations or Biases
- **Domain Bound Scope:** The system is explicitly restricted to numerical bounds based on user-selected difficulty levels (Easy: 1–20, Normal: 1–100, Hard: 1–50). It cannot interpret semantic natural language guesses or contextual text prompts.
- **Deterministic Randomness:** Relies on Python's pseudo-random number generator (`random.randint`), which lacks adaptive difficulty scaling or player-adaptive modeling.

---

## 2. Misuse Prevention & Guardrails
- **Potential Misuse:** Malicious users or scripts might attempt to inject SQL-like syntax, malicious strings, or massive overflow integers to break state management or crash the Streamlit web server.
- **Mitigation:** Comprehensive type-checking and defensive range-bounding in `parse_guess()` catch malformed inputs, returning safe, user-friendly error messages rather than propagating raw application exceptions or crashes.

---

## 3. Reliability & Testing Surprises
- **Testing Surprise:** During automated `pytest` implementation, we discovered that loose string casting (such as handling float strings like `"50.0"`) caused unhandled type errors when compared against integer secret keys.
- **Resolution:** Adding explicit float-to-integer parsing logic solved the edge case, proving that even simple AI-assisted applications require strict defensive programming for edge-case string formatting.

---

## 4. AI Collaboration Reflection
- **Collaboration Tool:** Gemini / AI coding assistant.
- **Accepted Suggestion:** The AI recommended structuring input validation around a clean return status tuple `(ok: bool, value: int|None, error: str|None)`. This cleanly separated input guardrails from core game logic and made unit testing straightforward.
- **Rejected/Modified Suggestion:** The AI initially suggested using an overly complex regular expression (regex) parsing engine to sanitize raw string input. I rejected this as over-engineered and harder to read for a simple number guessing game, choosing a simpler `try-except` integer/float conversion block combined with `.strip()` validation instead.
