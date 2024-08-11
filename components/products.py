import streamlit as st
from utils.gsheets_connect import get_products_sheet, get_categories_sheet, get_brands_sheet, init_google_auth
import re
import os

def show():
    st.header("Products Management")

    # Initialize Google authentication with credentials from secrets
    credentials_dict = st.secrets["google_sheets"]
    init_google_auth(credentials_dict)

    products_sheet = get_products_sheet()
    categories_sheet = get_categories_sheet()
    brands_sheet = get_brands_sheet()

    products = products_sheet.get_all_records()
    categories = categories_sheet.get_all_records()
    brands = brands_sheet.get_all_records()

    # Display existing products in card style
    st.subheader("Available Products")
    for product in products:
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                if product['Image']:
                    st.image(product['Image'], use_column_width=True)
                else:
                    st.markdown("📷 No Image")
            with col2:
                st.subheader(product['Product Name'])
                st.write(f"Category: {get_category_name(product['Category ID'], categories)}")
                st.write(f"Brand: {get_brand_name(product['Brand ID'], brands)}")
                st.write(f"Price: ${product['Price']}")
                st.write("Sizes & Quantities:")
                sizes = parse_size_quantity(product['Size & Quantity'])
                for size, quantity in sizes.items():
                    st.write(f"  {size}: {quantity}")

    # Add new product
    st.subheader("Add New Product")
    
    # Main container for the form
    with st.container():
        st.markdown("<div style='padding: 20px; border: 1px solid #ddd; border-radius: 10px;'>", unsafe_allow_html=True)
        
        # Add Image Box
        st.markdown(
            """
            <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 20px; border-radius: 5px; text-align: center;">
                <strong>Add Product Image</strong>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Product Form Fields
        new_product = {}
        new_product['Product ID'] = st.text_input("Product ID")
        new_product['Product Name'] = st.text_input("Product Name")
        new_product['Category ID'] = st.selectbox("Category", [c['Category ID'] for c in categories])
        new_product['Brand ID'] = st.selectbox("Brand", [b['Brand ID'] for b in brands])
        new_product['Price'] = st.number_input("Price", min_value=0.0, step=0.01)

        # Size & Quantity input
        sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
        size_quantities = {}
        for size in sizes:
            quantity = st.number_input(f"Quantity for {size}", min_value=0, step=1)
            if quantity > 0:
                size_quantities[size] = quantity
        new_product['Size & Quantity'] = format_size_quantity(size_quantities)

        # Image upload
        uploaded_file = st.file_uploader("Upload Product Image", type=['png', 'jpg', 'jpeg'])
        image_url = None
        if uploaded_file is not None:
            # Save the uploaded file temporarily
            temp_image_path = os.path.join("temp_images", uploaded_file.name)
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Uploaded {uploaded_file.name} successfully!")

            # Simulate uploading to cloud and getting the URL
            # In real application, upload to cloud and get the URL
            image_url = f"/mnt/data/{uploaded_file.name}"  # Placeholder path

        if st.button("Add Product"):
            if new_product['Product ID'] and new_product['Product Name']:
                # Use the image URL obtained after uploading
                if image_url is None:
                    image_url = "No Image"
                products_sheet.append_row([
                    new_product['Product ID'],
                    new_product['Product Name'],
                    new_product['Category ID'],
                    new_product['Brand ID'],
                    new_product['Price'],
                    new_product['Size & Quantity'],
                    image_url
                ])
                st.success("Product added successfully!")
            else:
                st.error("Please fill in all required fields.")

        st.markdown("</div>", unsafe_allow_html=True)

def get_category_name(category_id, categories):
    for category in categories:
        if category['Category ID'] == category_id:
            return category['Category Name']
    return "Unknown Category"

def get_brand_name(brand_id, brands):
    for brand in brands:
        if brand['Brand ID'] == brand_id:
            return brand['Brand Name']
    return "Unknown Brand"

def parse_size_quantity(size_quantity_str):
    # Parse the size and quantity string into a dictionary
    size_quantity_dict = {}
    pattern = r'\[(\w+),\s*(\d+)\]'
    matches = re.findall(pattern, size_quantity_str)
    for size, quantity in matches:
        size_quantity_dict[size] = int(quantity)
    return size_quantity_dict

def format_size_quantity(size_quantity_dict):
    # Format the size and quantity dictionary into a string
    return ', '.join(f'[{size}, {quantity}]' for size, quantity in size_quantity_dict.items())

# Call the show function to display the application
show()
