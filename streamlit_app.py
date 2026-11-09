import streamlit as st
from app.calculator import add, subtract, multiply, divide

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮"
)

st.title("🧮 Smart Calculator")
st.write("A simple calculator with automated CI/CD using CircleCI")

st.divider()

col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input("Enter first number", value=0.0)

with col2:
    number2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate", use_container_width=True):

    try:
        if operation == "Addition":
            result = add(number1, number2)

        elif operation == "Subtraction":
            result = subtract(number1, number2)

        elif operation == "Multiplication":
            result = multiply(number1, number2)

        else:
            result = divide(number1, number2)

        st.success(f"Result: {result}")

    except ValueError as e:
        st.error(str(e))