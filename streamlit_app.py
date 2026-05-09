# Import python packages.
import streamlit as st



from snowflake.snowpark.functions import col



st.title(f"Customize Your Smoothie :cup_with_straw: {st.__version__}")
st.write(
  """Choose the fruits you want in your custom Smoothie
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

name_of_order = st.text_input("Name of Smoothie")
st.write("The name of your smoothie will be:", name_of_order)

##session = get_active_session() pruebas github
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_lst = st.multiselect('choose up to 5 ingrdients:', my_dataframe, max_selections=5)

if ingredients_lst:
    #st.write(ingredients_lst)
    #st.text(ingredients_lst)
    ingredients_string = ''

    for fruit_choosen in ingredients_lst:
        ingredients_string += fruit_choosen + ' '
#
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders (name_on_order,ingredients )
                    values ('""" + name_of_order + """','""" + ingredients_string + """')"""

    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
    

        if ingredients_string:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered! ' + name_of_order, icon="✅")

        #st.write(my_insert_stmt)

