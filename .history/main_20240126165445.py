import streamlit as st
# from fawkes import Fawkes
import tempfile
import os


def main():
    st.title("Fawkes: Protecting Privacy against Unauthorized Deep Learning Models")
    st.write("Fawkes is a system for disguising images to evade facial recognition.")
    st.write(
        "This is a demo of the Fawkes algorithm. You can upload an image and see how it is disguised."
    )
    st.write(
        "You can also download the disguised image and use it on social media to protect your privacy."
    )

    # create a file upload
    uploaded_file = st.file_uploader("Choose an image...", type=["png"])
    # Save the uploaded file to a temporary file inside its own temp dir
    if uploaded_file:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.write("Saved uploaded image to temp dir: ")
            st.image(temp_file_path)


if __name__ == "__main__":
    main()