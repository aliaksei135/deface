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
    # Save the uploaded file to a temporary directory
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            st.write("Saved file to", tmp_file.name)
            image_paths = [tmp_file.name]
            # my_fawkes = Fawkes("extractor_2", "0", 1)
            # status = my_fawkes.run_protection(image_paths)
            # st.image(status[0], caption="Original Image", use_column_width=True)
            # st.image(status[1], caption="Cloaked Image", use_column_width=True)
            # st.write("Download the cloaked image:")
            # st.download_button(
            #     label="Download Cloaked Image",
            #     data=status[1],
            #     file_name="cloaked_image.png",
            #     mime="image/png",
            # )

if __