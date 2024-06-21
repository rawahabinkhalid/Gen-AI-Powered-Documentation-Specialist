import os
import warnings
import mammoth
from datetime import datetime
import gradio as gr
from common_crew_functions import setup_environment, load_template, call_crew_kickoff

warnings.filterwarnings('ignore')

# Setup environment variables and load the BRD template
setup_environment()
cleaned_brd_template = load_template('./brd-template/brd-template.md')

def process_file(input_file):
    if input_file is not None:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        filename = f'meeting-transcription/meeting-transcript_{current_datetime}.md'
        
        with open(input_file, "rb") as docx_file:
            result = mammoth.convert_to_markdown(docx_file)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result.value)
                f.close()

        response = call_crew_kickoff(current_datetime, cleaned_brd_template)
        
        output_filename = f"generated-brd/generated-brd_{current_datetime}.md"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(response)
        
        return output_filename, response

with gr.Blocks() as demo:
    gr.Markdown("# Gen AI Powered Documentation Specialist - Business Requirement Document (BRD) Generation")
    gr.Markdown("Upload your `.docx` meeting transcript to generate a Business Requirements Document (BRD).")
    with gr.Row():
        file_input = gr.File(label="Upload the meeting transcript (.docx file supported only)", file_types=[".docx"])
        download_btn = gr.File(label="Download Processed Business Requirement Document (BRD) in Markdown")
        
    with gr.Row():
        markdown_output = gr.Markdown()

    file_input.change(process_file, inputs=file_input, outputs=[download_btn, markdown_output])

demo.launch()
