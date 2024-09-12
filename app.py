import streamlit as st
from datetime import datetime, time

# Função principal para o frontend
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow")

    # Campos de entrada para os dados
    email = st.text_input("Email do Vendedor")
    data = st.date_input("Data da compra", datetime.now())
    time = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    product_value = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantity = st.number_input("Quantidade de produtos", min_value=1, step=1)
    product_type = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama 3.0"])

    # Botão de submissão
    if st.button("Salvar"):
        # Combinando a data e hora selecionadas para criar o datetime
        date_time = datetime.combine(data, hora)

        # Exibindo os dados na tela
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Compra: {date_time}")
        st.write(f"Valor da Venda: R$ {product_value:.2f}")
        st.write(f"Quantidade de Produtos: {quantity}")
        st.write(f"Produto: {product_type}")

if __name__ == "__main__":
    main()