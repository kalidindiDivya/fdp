import streamlit as st

st.markdown(
	"""
	<style>
	.stApp { background-color: #e6ffed; }
	h1 { color: #C71585 !important; }
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown("<h1>BVC 2026 Admissions</h1>", unsafe_allow_html=True)
st.markdown(
	"<p style='color:#C71585; font-size:18px;'>Apply now for the 2026 academic year at BVC College!</p>",
	unsafe_allow_html=True,
)
st.image("adm.png", caption="Join BVC College Today!")