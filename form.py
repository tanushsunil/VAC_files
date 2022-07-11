import email
import streamlit as st
import sqlite3

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

def addData(a, b, c, d):
    cur.execute(
        """CREATE TABLE IF NOT EXISTS email_form(NAME TEXT(50), AGE TEXT(50), EMAIL TEXT(60));""")
    cur.execute("INSERT INTO email_form VALUES (?,?,?,?)", (a, b, c, d))
    conn.commit()
    conn.close()
    st.success("Successfully submitted")

def main():
    st.write("Chance short film Competition")
    with st.form(keys="Information form"):
        name = st.text_input("Enter your name :")
        age = st.text_input("Enter your age :")
        email = st.text_input("Enter your Email-ID :")
        submission = st.form_submit_button(label="Submit")
        if submission == True:
           addData(name, age, email)    

if __name__ == '__main__':
    main()

