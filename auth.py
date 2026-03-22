import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        st.login("google")
    st.stop()

st.markdown(f"Welcome! {st.user.name}")
st.image(st.user.picture, width=50)

st.markdown(f"""Some things about you:
- Google ID: {st.user.sub}
- Given Name: {st.user.given_name}
- Family Name: {st.user.family_name}
- Email: {st.user.email} ({st.user.email_verified})
""")

if st.user.is_logged_in and st.button("Log out"):
    st.logout()
