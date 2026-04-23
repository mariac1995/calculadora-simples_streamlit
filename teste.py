import streamlit as st

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b


st.title("Mini Calculadora")

operacao = st.selectbox(
    "Escolha a operação:",
    ("Soma", "Subtração", "Multiplicação", "Divisão")
)

num1 = st.number_input("Digite o primeiro número")
num2 = st.number_input("Digite o segundo número")

if st.button("Calcular"):

    if operacao == "Soma":
        resultado = somar(num1, num2)

    elif operacao == "Subtração":
        resultado = subtrair(num1, num2)

    elif operacao == "Multiplicação":
        resultado = multiplicar(num1, num2)

    elif operacao == "Divisão":
        resultado = dividir(num1, num2)

    if isinstance(resultado, str):
        st.error(resultado)
    else:
        st.success(f"Resultado: {resultado:.2f}")