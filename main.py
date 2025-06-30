# save as app.py
import streamlit as st
import random
import hashlib

def generate_two_digit(seed_string):
    hash_obj = hashlib.sha256(seed_string.strip().lower().encode())
    numeric_seed = int(hash_obj.hexdigest(), 16)
    random.seed(numeric_seed)
    return random.randint(10, 99)

st.title("Your number for 4001 A2")

email = st.text_input("Enter your email address")

if email:
    number = generate_two_digit(email)
    st.success(f"Your individual assignment number is: **{number}**")
