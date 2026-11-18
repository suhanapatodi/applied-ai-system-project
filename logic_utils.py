def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Hard":
        return 1, 50
    return 1, 100  # Default / Normal


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess with robust input guardrails.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or str(raw).strip() == "":
        return False, None, "Enter a guess."

    try:
        raw_str = str(raw).strip()
        value = int(float(raw_str)) if "." in raw_str else int(raw_str)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).
    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return ("Win", "Congratulations! You guessed the correct number!")
    elif guess > secret:
        return ("Too High", "Your guess is too high! Try lower.")
    else:
        return ("Too Low", "Your guess is too low! Try higher.")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points
    return current_score - 5


def generate_ai_coach_hint(guess_history: list, secret: int, low: int, high: int) -> dict:
    """
    Agentic AI Feature (RAG-lite & Reasoning Coach):
    Analyzes player guess history, retrieves context (distance & strategy), 
    generates an AI coaching hint, and applies guardrails.
    """
    if not guess_history:
        return {
            "status": "active",
            "confidence": 1.0,
            "advice": f"AI Coach initialized. Range is {low} to {high}. Make your opening move!"
        }

    latest_guess = guess_history[-1]
    distance = abs(latest_guess - secret)
    span = high - low

    # RAG / Retrieval of dynamic strategy context based on distance ratio
    ratio = distance / span
    if ratio > 0.4:
        strategy_context = "Strategy Rule: You are far off. Consider utilizing a binary search midpoint strategy to cut the search space in half."
    elif ratio > 0.15:
        strategy_context = "Strategy Rule: Warm! You are within moderate range. Adjust your increments carefully."
    else:
        strategy_context = "Strategy Rule: Boiling hot! You are extremely close to the secret number."

    # Agentic Guardrail & Reasoning check
    if latest_guess == secret:
        ai_message = "AI Coach: Target acquired! Optimal solution reached."
        confidence = 1.0
    elif latest_guess > secret:
        ai_message = f"AI Coach Analysis: {latest_guess} was too high. {strategy_context}"
        confidence = 0.95
    else:
        ai_message = f"AI Coach Analysis: {latest_guess} was too low. {strategy_context}"
        confidence = 0.95

    return {
        "status": "success",
        "confidence": confidence,
        "advice": ai_message
    }
