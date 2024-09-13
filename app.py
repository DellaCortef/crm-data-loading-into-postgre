import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError
from database import load_into_postgre
from contract import Sales, ProductEnum

# Main function for the frontend
def main():
    st.title("ZapFlow CRM and Sales System")

    # Input fields for data
    seller_email = st.text_input("Email do Vendedor")
    purchase_data = st.date_input("Data da compra", datetime.now())
    purchase_time = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    product_value = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    product_quantity = st.number_input("Quantidade de produtos", min_value=1, step=1)
    product_type = st.selectbox("Produto", options=[e.value for e in ProductEnum])

    # Submit button
    if st.button("Salvar"):

        try:

            # Combining the selected date and time to create the datetime
            date_time = datetime.combine(purchase_data, purchase_time)

            # Validating data with Pydantic
            sale = Sales(
                email = seller_email.lower(),
                date_time = date_time,
                product_value = product_value,
                product_quantity = product_quantity,
                product_type = product_type.lower()
            )
            st.write(sale)
            load_into_postgre(sale)

        except ValidationError as e:
            st.error(f"Something went wrong: {e}")
        
        except Exception as e:
            st.error(f"Error saving data: {e}")

if __name__ == "__main__":
    main()