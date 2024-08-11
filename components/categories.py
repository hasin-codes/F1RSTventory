import streamlit as st
from utils.gsheets_connect import get_categories_sheet

def show():
    st.header("Categories Management")
    sheet = get_categories_sheet()

    # List existing categories
    st.subheader("Existing Categories")
    categories = sheet.get_all_records()
    for category in categories:
        st.text(f"{category['Category ID']}: {category['Category Name']}")

    # Add new category
    st.subheader("Add New Category")
    new_category = st.text_input("Enter new category name")
    if st.button("Add Category"):
        if new_category:
            new_id = len(categories) + 1
            sheet.append_row([new_id, new_category])
            st.success(f"Category {new_category} added successfully!")
        else:
            st.error("Please enter a category name.")

    # Edit category
    st.subheader("Edit Category")
    category_to_edit = st.selectbox("Select category to edit", [category['Category Name'] for category in categories])
    new_category_name = st.text_input("Enter new name for the category")
    if st.button("Update Category"):
        if new_category_name:
            for idx, category in enumerate(categories):
                if category['Category Name'] == category_to_edit:
                    sheet.update_cell(idx+2, 2, new_category_name)
                    st.success(f"Category updated from {category_to_edit} to {new_category_name}")
                    break
        else:
            st.error("Please enter a new name for the category.")

    # Delete category
    st.subheader("Delete Category")
    category_to_delete = st.selectbox("Select category to delete", [category['Category Name'] for category in categories])
    if st.button("Delete Category"):
        for idx, category in enumerate(categories):
            if category['Category Name'] == category_to_delete:
                sheet.delete_rows(idx+2)
                st.success(f"Category {category_to_delete} deleted successfully!")
                break