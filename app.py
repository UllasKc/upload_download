import streamlit as st
import zipfile
import os
import io

# Function to upload and process a zip file
def upload_zip():
    st.title("Upload and Download ZIP File")

    # Upload the ZIP file
    uploaded_file = st.file_uploader("Choose a ZIP file", type="zip")

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        
        # Display the content of the ZIP file
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            st.write("Files in the ZIP:")
            for file_name in file_list:
                st.write(file_name)
            
            # Extract the files in memory
            st.write("Extracting files...")
            extracted_files = {name: zip_ref.read(name) for name in file_list}
        
        # Option to download the extracted files as a new ZIP
        if st.button("Download ZIP"):
            download_zip(file_list, extracted_files)
    else:
        st.info("Please upload a ZIP file to proceed.")

# Function to create and download a new ZIP file
def download_zip(file_list, extracted_files):
    # Create a ZIP file in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for file_name, data in extracted_files.items():
            zip_file.writestr(file_name, data)

    zip_buffer.seek(0)
    
    # Stream the ZIP file to the browser for download
    st.download_button(
        label="Download ZIP",
        data=zip_buffer,
        file_name="downloaded.zip",
        mime="application/zip"
    )

# Run the app
if __name__ == "__main__":
    upload_zip()
