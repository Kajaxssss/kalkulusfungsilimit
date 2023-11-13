import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, limit

def main():
    st.title("Kalkulator Limit")

    # Input fungsi
    st.subheader("Masukkan fungsi limit:")
    function_input = st.text_input("f(x) =", "x**2 - 1")

    # Input nilai x
    st.subheader("Masukan nilai x:")
    x_value = st.number_input("x =", value=1.0)

    # Hitung limit
    try:
        x = symbols('x')
        f = eval(function_input)
        limit_value = limit(f, x, x_value)
        st.success(f"Limit of {function_input} as x approaches {x_value}: {limit_value}")
        
        # Plot grafik fungsi
        plot_function(f, x_value)

    except Exception as e:
        st.error("Error: Invalid input or calculation")

def plot_function(f, x_value):
    x_vals = np.linspace(float(x_value) - 2, float(x_value) + 2, 400)
    y_vals = [f.subs('x', val) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {f}')
    plt.scatter(float(x_value), float(f.subs('x', x_value)), color='red', label=f'x = {x_value}')

    plt.axvline(x=float(x_value), color='gray', linestyle='--', label='Approaching x')
    plt.axhline(y=float(f.subs('x', x_value)), color='gray', linestyle='--')

    plt.title("Graph of the Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    st.pyplot(plt)

    st.write("")
st.caption("Edited by Afif Kisnandhya Putra")
st.caption("Source: https://github.com/felipeph/streamlit-function")


    
if __name__ == "__main__":
    main()