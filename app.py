import streamlit as st

# Streamlit App Title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator App")

st.write("Enter two numbers and select an operation to perform:")

# Input fields
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Button to calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
