import streamlit as st
from fawkes import Fawkes
import tempfile
import os


# @st.cache_resource
def get_fawkes():
    protector = Fawkes("extractor_2", "cpu", 1)
    return protector


def main():
    st.title("Deface")
    st.write("Fawkes is a system for disguising images to evade facial recognition.")
    st.write(
        "This is a deployed version of the Fawkes system. You can upload an image and cloak it to protect your privacy."
    )
    st.write(
        "You can download the disguised image and use it on social media to protect your privacy."
    )

    # create a file upload
    uploaded_file = st.file_uploader("Choose an image...", type=["png"])
    # Save the uploaded file to a temporary file inside its own temp dir
    if uploaded_file:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            with st.spinner("Cloaking image..."):
                protector = get_fawkes()
                status = protector.run_protection([temp_file_path])
            if status == 1:
                # Get the cloaked image named <name>_cloaked.<ext>
                cloaked_image_path = temp_file_path.split(".")[0] + "_cloaked.png"
                # Download the cloaked image
                st.download_button(
                    label="Download cloaked image",
                    data=cloaked_image_path,
                    file_name=f"{uploaded_file.name.split('.')[0]}_cloaked.png",
                )
                st.write("Cloaked image: ")
                st.image(cloaked_image_path)
            else:
                st.write("Failed to cloak image")
                st.write("Error code: ", status)


if __name__ == "__main__":
    main()
