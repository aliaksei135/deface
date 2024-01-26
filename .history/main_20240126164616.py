import streamlit as st
from fawkes import Fawkes


def main():
    st.title("Fawkes: Protecting Privacy against Unauthorized Deep Learning Models")
    st.write("Fawkes is a system for disguising images to evade facial recognition.")
    st.write("This is a demo of the Fawkes algorithm. You can upload an image and see how it is disguised.")
    st.write("You can also download the disguised image and use it on social media to protect your privacy.")
    
     if self.my_fawkes is None:
            self.my_fawkes = Fawkes("extractor_2", '0', 1)
        status = self.my_fawkes.run_protection(self.image_paths, debug=True)