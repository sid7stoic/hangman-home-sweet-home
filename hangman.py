import streamlit as st
import random

st.title("🏡 Hangman: Home Sweet Home Edition")

# Initial setup
word_list = ["Ramya", "Praveen", "Ishani", "Siddharth", "Nirved", "Nidhin", "Shruthi", "Ragini", "Sreedharan"]
stages = ["🪦", "😵", "😰", "😐", "🙂", "😀", "😎"]

# Initialize session state
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.display = ["_" for _ in st.session_state.chosen_word]
    st.session_state.lives = 6
    st.session_state.correct_guesses = []
    st.session_state.game_over = False

# Display word
st.markdown("### Word to guess:")
st.write(" ".join(st.session_state.display))

# Input guess
guess = st.text_input("Guess a letter:").lower()

if guess and not st.session_state.game_over:
    if guess in st.session_state.correct_guesses:
        st.warning(f"You already guessed '{guess}'. Try another letter.")
    else:
        st.session_state.correct_guesses.append(guess)

        if guess in st.session_state.chosen_word.lower():
            for idx, letter in enumerate(st.session_state.chosen_word):
                if letter.lower() == guess:
                    st.session_state.display[idx] = letter
        else:
            st.session_state.lives -= 1
            st.error(f"'{guess}' is not in the word. You lost a life!")

# Show game status
st.markdown("### Current Status:")
st.write(" ".join(st.session_state.display))
st.write(f"Lives left: {st.session_state.lives}")
st.write(stages[st.session_state.lives])

# Win/Lose logic
if "_" not in st.session_state.display and not st.session_state.game_over:
    st.balloons()
    st.success("🎉 YOU WIN!")
    st.session_state.game_over = True

if st.session_state.lives == 0 and not st.session_state.game_over:
    st.error(f"💀 YOU LOSE! The word was: {st.session_state.chosen_word}")
    st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.clear()
        st.experimental_rerun()
