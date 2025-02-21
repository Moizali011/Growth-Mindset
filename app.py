#stream
import streamlit as st

st.set_page_config(page_title="Growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge: Web App With Streamlit ")


st.header("🚀Welcome to your Growth Journey!")
st.write("Embrance challenges,learn from mistakes,and unlock your full potential.This Ai-powered app helps you build a growth mindset with reflection,challenges,and achievement!")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal: it is the courage to continue that counts,-Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


if user_input:
    st.success(f"youre facing: {user_input}. keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")


st.header("Reflection on your Learning")
reflection = st.text_area("Write your reflections here:")


if reflection:
    st.success(f"Great Insight! your reflection:{reflection}")

else:
    st.info("Reflection on past experience help you grow! share your difficulties")

st.header("Celebrate your Wins!")

acheivment = st.text_input("Share something you've recently accomplished:")


if acheivment:
    st.success(f"🌟Amazing! You achieved:{acheivment}")

else:
    st.info("Big or Small , every acheivment counts! share one now!😍")

st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination!💐")
st.write("⛔ Created by Moiz Ali")        