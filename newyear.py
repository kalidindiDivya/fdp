import streamlit as st

st.markdown(
		"""
		<style>
		.stApp { background-color: #FFDAB9 !important; }
		h1 {
			font-family: 'Brush Script MT', 'Lucida Handwriting', cursive;
			font-weight: 700;
			font-style: italic;
			color: #2F4F4F !important;
		}
		p {
			color: #FF8C00 !important;
		}
		</style>
		""",
		unsafe_allow_html=True,
)

st.markdown("<h1>2026 New Year Celebration at BVC College</h1>", unsafe_allow_html=True)
st.markdown(
		"<p>Join us in welcoming the new year with exciting events and activities at BVC College!</p>",
		unsafe_allow_html=True,
)
st.image("newyear.png", caption="Celebrate the New Year with Us!")
st.markdown(
		"<p>Don't miss out on the fun and festivities. Let's make this new year memorable together!</p>",
		unsafe_allow_html=True,
)