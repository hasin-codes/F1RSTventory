import streamlit as st
from utils.gsheets_connect import get_brands_sheet

def show():
    st.header("Brands Management")
    sheet = get_brands_sheet()

    # List existing brands
    st.subheader("Existing Brands")
    brands = sheet.get_all_records()
    for brand in brands:
        st.text(f"{brand['Brand ID']}: {brand['Brand Name']}")

    # Add new brand
    st.subheader("Add New Brand")
    new_brand = st.text_input("Enter new brand name")
    if st.button("Add Brand"):
        if new_brand:
            new_id = len(brands) + 1
            sheet.append_row([new_id, new_brand])
            st.success(f"Brand {new_brand} added successfully!")
        else:
            st.error("Please enter a brand name.")

    # Edit brand
    st.subheader("Edit Brand")
    brand_to_edit = st.selectbox("Select brand to edit", [brand['Brand Name'] for brand in brands])
    new_brand_name = st.text_input("Enter new name for the brand")
    if st.button("Update Brand"):
        if new_brand_name:
            for idx, brand in enumerate(brands):
                if brand['Brand Name'] == brand_to_edit:
                    sheet.update_cell(idx+2, 2, new_brand_name)
                    st.success(f"Brand updated from {brand_to_edit} to {new_brand_name}")
                    break
        else:
            st.error("Please enter a new name for the brand.")

    # Delete brand
    st.subheader("Delete Brand")
    brand_to_delete = st.selectbox("Select brand to delete", [brand['Brand Name'] for brand in brands])
    if st.button("Delete Brand"):
        for idx, brand in enumerate(brands):
            if brand['Brand Name'] == brand_to_delete:
                sheet.delete_rows(idx+2)
                st.success(f"Brand {brand_to_delete} deleted successfully!")
                break