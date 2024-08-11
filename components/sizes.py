import streamlit as st
from utils.gsheets_connect import get_sizes_sheet

def show():
    st.header("Sizes Management")
    sheet = get_sizes_sheet()

    # List existing sizes
    st.subheader("Existing Sizes")
    sizes = sheet.get_all_records()
    for size in sizes:
        st.text(f"{size['Size ID']}: {size['Size Name']}")

    # Add new size
    st.subheader("Add New Size")
    new_size = st.text_input("Enter new size")
    if st.button("Add Size"):
        if new_size:
            new_id = len(sizes) + 1
            sheet.append_row([new_id, new_size])
            st.success(f"Size {new_size} added successfully!")
        else:
            st.error("Please enter a size.")

    # Edit size
    st.subheader("Edit Size")
    size_to_edit = st.selectbox("Select size to edit", [size['Size Name'] for size in sizes])
    new_size_name = st.text_input("Enter new name for the size")
    if st.button("Update Size"):
        if new_size_name:
            for idx, size in enumerate(sizes):
                if size['Size Name'] == size_to_edit:
                    sheet.update_cell(idx+2, 2, new_size_name)  # +2 because sheet is 1-indexed and has a header
                    st.success(f"Size updated from {size_to_edit} to {new_size_name}")
                    break
        else:
            st.error("Please enter a new name for the size.")

    # Delete size
    st.subheader("Delete Size")
    size_to_delete = st.selectbox("Select size to delete", [size['Size Name'] for size in sizes])
    if st.button("Delete Size"):
        for idx, size in enumerate(sizes):
            if size['Size Name'] == size_to_delete:
                sheet.delete_rows(idx+2)  # +2 because sheet is 1-indexed and has a header
                st.success(f"Size {size_to_delete} deleted successfully!")
                break