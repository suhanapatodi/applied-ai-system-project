import streamlit as st
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
    generate_ai_coach_hint,
)

st.title("🕵️ Game Glitch Investigator Pro: AI-Powered Edition")

# Initialize session state
if "secret" not in st.session_state:
    st.session_state.difficulty = "Normal"
    low, high = get_range_for_difficulty(st.session_state.difficulty)
    import random
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.guess_history = []
    st.session_state.game_over = False

difficulty = st.selectbox("Select Difficulty", ["Easy", "Normal", "Hard"], index=1)
if difficulty != st.session_state.difficulty:
    st.session_state.difficulty = difficulty
    low, high = get_range_for_difficulty(difficulty)
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.guess_history = []
    st.session_state.game_over = False

low, high = get_range_for_difficulty(st.session_state.difficulty)
st.write(f"Guess the secret number between **{low}** and **{high}**!")

# Display AI Agent Coach status
ai_feedback = generate_ai_coach_hint(
    st.session_state.guess_history, 
    st.session_state.secret, 
    low, 
    high
)
st.info(f"🤖 **AI Strategy Coach:** {ai_feedback['advice']} *(Confidence: {ai_feedback['confidence']})*")

# User input form
with st.form("guess_form", clear_on_submit=True):
    raw_input = st.text_input("Enter your guess:")
    submitted = st.form_submit_button("Submit Guess")

if submitted and not st.session_state.game_over:
    ok, guess_val, err_msg = parse_guess(raw_input, low, high)
    if not ok:
        st.error(err_msg)
    else:
        st.session_state.attempts += 1
        st.session_state.guess_history.append(guess_val)
        outcome, msg = check_guess(guess_val, st.session_state.secret)
        st.session_state.score = update_score(
            st.session_state.score, outcome, st.session_state.attempts
        )
        
        if outcome == "Win":
            st.success(f"{msg} Total attempts: {st.session_state.attempts}")
            st.session_state.game_over = True
        elif outcome == "Too High":
            st.warning(msg)
        else:
            st.info(msg)

st.write(f"**Score:** {st.session_state.score} | **Attempts:** {st.session_state.attempts}")

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret = random.randint(low, high)
        st.session_state.attempts = 0
        st.session_state.guess_history = []
        st.session_state.game_over = False
        st.rerun()
