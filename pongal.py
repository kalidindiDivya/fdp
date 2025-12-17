import streamlit as st

st.markdown(
	"""
	<style>
	.stApp { background-color: inherit; }
	h1 { color: #0000FF !important; }
	h2, h3, p { color: #C71585 !important; }
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown("<h1>pongal Celebration at BVC College</h1>", unsafe_allow_html=True)

st.markdown(
	"<p>Join us in celebrating Pongal with traditional festivities and fun activities at BVC College!</p>",
	unsafe_allow_html=True,
)
st.markdown(
	"<p>Experience the joy of Pongal with cultural performances, delicious food, and vibrant decorations.</p>",
	unsafe_allow_html=True,
)
st.image("pongal.png", caption="Celebrate Pongal with Us!")
st.markdown(
	"<p>Let's come together to honor this harvest festival and create unforgettable memories!</p>",
	unsafe_allow_html=True,
)