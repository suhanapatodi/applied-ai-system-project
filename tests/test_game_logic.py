from logic_utils import check_guess, parse_guess, generate_ai_coach_hint

def test_winning_guess():
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_edge_case_string_and_empty_inputs():
    ok, val, err = parse_guess("", 1, 100)
    assert not ok
    assert err == "Enter a guess."

def test_edge_case_out_of_bounds_numbers():
    ok, val, err = parse_guess("150", 1, 100)
    assert not ok
    assert "between 1 and 100" in err

def test_ai_coach_agent_hint():
    """Verify that the AI agent coach analyzes history and returns strategic advice with confidence."""
    history = [20, 80, 50]
    response = generate_ai_coach_hint(history, 50, 1, 100)
    assert response["status"] == "success"
    assert response["confidence"] == 1.0
    assert "Target acquired" in response["advice"]
