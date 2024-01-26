import streamlit as st
# from fawkes import Fawkes
import tempfile


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
    # Save the uploaded file to a temporary file inside a temporary directory

if __name__ == "__main__":
    main()