import streamlit as st

# Page title
st.set_page_config(page_title="Murder Mystery")

# Game data
victim = "Professor Black"

suspects = [
    {
        "name": "Alice",
        "alibi": "I was reading in the library."
    },
    {
        "name": "Bob",
        "alibi": "I was fixing my car in the garage."
    },
    {
        "name": "Charlie",
        "alibi": "I was walking in the garden."
    }
]

clues = [
    "A muddy footprint was found.",
    "A torn glove was discovered.",
    "Someone heard an argument."
]

murderer = "Bob"

# Score
if "score" not in st.session_state:
    st.session_state.score = 0

# Title
st.title("🕵️ Murder Mystery Game")

st.write("Solve the mystery and find the murderer!")

# Sidebar
st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Choose",
    ["Case File", "Suspects", "Clues", "Accuse"]
)

st.sidebar.write("Score:", st.session_state.score)

# Case File Page
if page == "Case File":

    st.header("Victim")

    st.write(victim)

    st.write(
        """
        A murder has happened.
        
        Check the suspects,
        read the clues,
        and solve the case.
        """
    )

# Suspects Page
elif page == "Suspects":

    st.header("Suspects")

    for suspect in suspects:

        st.subheader(suspect["name"])

        st.write("Alibi:")

        st.write(suspect["alibi"])

        st.divider()

# Clues Page
elif page == "Clues":

    st.header("Clues")

    for clue in clues:

        st.write("🔍", clue)

# Accuse Page
elif page == "Accuse":

    st.header("Make an Accusation")

    suspect_names = []

    for suspect in suspects:
        suspect_names.append(suspect["name"])

    guess = st.selectbox(
        "Who is the murderer?",
        suspect_names
    )

    if st.button("Accuse"):

        if guess == murderer:

            st.success("🎉 Correct!")

            st.session_state.score += 20

        else:

            st.error(
                f"Wrong! The murderer was {murderer}"
            )

        st.write(
            "Score:",
            st.session_state.score
        )
!streamlit run app.py
