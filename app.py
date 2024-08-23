import streamlit as st
import zipfile
import os
from pathlib import Path

# Define the path where uploaded files will be saved
SAVE_DIR = Path("uploaded_files")

# Ensure the directory exists
SAVE_DIR.mkdir(parents=True, exist_ok=True)

def list_files_in_directory(directory):
    """Returns a list of files in the given directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(directory / f)]

# Function to handle file upload and save it to the local path
def upload_zip_file():
    st.title("Upload and Download ZIP File")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a ZIP file", type="zip")

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        
        # Save the uploaded file to the specified directory
        save_path = SAVE_DIR / uploaded_file.name
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write(f"File saved to {save_path}")
        
        # Extract the ZIP file content (optional)
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            st.write("Files in the ZIP:")
            for file_name in file_list:
                st.write(file_name)

# Function to display download button if there are files in the directory
def download_zip_file():
    st.title("Download Available ZIP Files")

    # List files in the directory
    files = list_files_in_directory(SAVE_DIR)
    
    if files:
        for file_name in files:
            file_path = SAVE_DIR / file_name
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"Download {file_name}",
                    data=f,
                    file_name=file_name,
                    mime="application/zip"
                )
    else:
        st.info("No files available for download.")

# Run the app
if __name__ == "__main__":
    # Display both upload and download sections
    upload_zip_file()
    st.markdown("---")
    download_zip_file()
