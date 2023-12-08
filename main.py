import streamlit as st

def largest_among_three(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Among Three Numbers")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        largest = largest_among_three(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
