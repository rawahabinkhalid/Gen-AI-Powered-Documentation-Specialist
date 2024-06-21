import streamlit as st
import os
import warnings
import mammoth
from datetime import datetime
from io import BytesIO
from dotenv import load_dotenv
from common_crew_functions import setup_environment, load_template, call_crew_kickoff

warnings.filterwarnings('ignore')

# Setup environment variables and load the BRD template
setup_environment()
cleaned_brd_template = load_template('./brd-template/brd-template.md')

def process_file(input_file):
    if input_file is not None:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        filename = f'meeting-transcription/meeting-transcript_{current_datetime}.md'

        with BytesIO(input_file.getvalue()) as docx_file:
            result = mammoth.convert_to_markdown(docx_file)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result.value)

        response = call_crew_kickoff(current_datetime, cleaned_brd_template)

        output_filename = f"generated-brd/generated-brd_{current_datetime}.md"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(response)

        return output_filename, response

st.set_page_config(layout="wide")
st.title("Gen AI Powered Documentation Specialist - Business Requirement Document (BRD) Generation")
st.write("Upload your meeting transcript in `.docx` format to generate a Business Requirements Document (BRD).")

uploaded_file = st.file_uploader("Choose a .docx file", type=["docx"])

# Load SVG from local assets folder
with open("./assets/Spinner@1x-1.0s-200px-200px.svg", "r") as svg_file:
    svg = svg_file.read()

# Custom CSS to create the backdrop and style the loader
st.markdown("""
<style>
div.stButton > button:first-child {
    color: #4CAF50;
}
.css-18e3th9 {
    align-items: center;
    justify-content: center;
    display: flex;
    height: 100vh;
    width: 100vw;
    position: fixed;
    top: 0;
    left: 0;
    background-color: rgba(0,0,0,0.5);
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)
if uploaded_file is not None:

    
    loader_placeholder = st.empty()  # Create an empty placeholder
    loader_placeholder.markdown(f"""
    <div class="css-18e3th9">
        <div style="text-align: center;">
            {svg}
            <!-- <div style="padding-top:101.053%;position:relative;"><iframe src="https://upload.wikimedia.org/wikipedia/commons/b/b6/Loading_2_transparent.gif" width="100%" height="100%" style='position:absolute;top:0;left:0;pointer-events:none;background:transparent;' frameBorder="0" allowFullScreen></iframe></div> -->
            <!-- <img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif" alt="Loading..." style="width: 100px; height: 100px;"> -->
            <p><strong>Please wait...</br>Processing the document</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    # Process the file
    output_filename, response = process_file(uploaded_file)
    loader_placeholder.empty()  # Remove the loader placeholder after processing is complete

    st.success(f"Business Requirement Document (BRD) has been generated and saved as: {output_filename}")
    st.download_button("Download Business Requirement Document (BRD) File", open(output_filename, 'r').read(), file_name=output_filename, mime='text/markdown')
    st.markdown(response)
