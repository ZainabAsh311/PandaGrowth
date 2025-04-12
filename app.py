#streamlit
import streamlit as st

st.set_page_config (page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with streamlit")

st.header("🌃Welcome to your Growth Journey!")
st.write("Enbrace Challenges, learn from mistakes, and unlock your full potential. This AI-powered app help!")

#quote section
st.header("📝Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts")

st.header("˗ˏˋ꒰ 🍒 ꒱ What's Your Challenge Today?")
user_input=st.text_input("Describe a challenge You're Facing:")

#Condition
if user_input:
    st.success(f"you're facing: {user_input}. keep Pushing Forward Towards Your Goal!🌞")
else:
    st.warning("Tell us about your Challenge to get Started!")


#Reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your Reflections here")

if reflection:
    st.success(f" Great Insight! your reflection: {reflection}")
else:
    st.info("Reflecting on Past Experience help you grow! Share your difficulties")

#achievement
st.header("🔑 Celebrate Your Wins!")
achievement= st.text_input ("Share something you've recently accomplished:")

if achievement:
    st.success(f"✨Amazing! You acheived: {achievement}")
else: 
    st.info("Big or Small, every acheivment counts! Share one now 😍")

#footer
st.write("- - -")
st.write("🌟Keep Believing in Yourself. Growth is a Journey, not a destination🌟")
st.write("***🎯Created by Zainab Ashraf***")
