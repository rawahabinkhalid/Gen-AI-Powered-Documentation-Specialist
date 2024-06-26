---
title: Gen AI Powered Documentation Specialist
emoji: 📈
colorFrom: pink
colorTo: blue
sdk: gradio
sdk_version: 4.36.0
app_file: app.py
pinned: false
---

# Gen AI Powered Documentation Specialist - Business Requirement Document (BRD) Generation

## Overview

This project is a Proof of Concept (POC) for a "Gen AI Powered Documentation Specialist" focused on generating Business Requirement Documents (BRDs) using CrewAI. The goal is to automate the extraction and structuring of key information from meeting transcripts to create comprehensive BRDs.

## Features

- **Automated Business Requirement Document (BRD) Generation**: Utilizes advanced AI agents to analyze meeting transcripts and produce well-structured BRDs.
- **Agent Roles**: Includes a Business Analyst agent and a Subject Matter Expert (SME) agent to ensure both functional and technical requirements are accurately captured.
- **Semantic Search and File Read Tools**: Enhances the agents' capabilities to process and extract relevant information from transcripts.
- **Gradio Interface**: Provides an easy-to-use web interface for uploading meeting transcripts and displaying the generated BRD.

## Requirements

- Python 3.8+
- OpenAI API Key
- Gradio
- Mammoth
- CrewAI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rawahabinkhalid/gen-ai-doc-specialist.git
    cd gen-ai-doc-specialist
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the project root and add your OpenAI API key:

    ```
    openai_api_key=YOUR_OPENAI_API_KEY
    ```

## Usage

1. Ensure you have a meeting transcript in `.docx` format ready for processing.

2. For Gradio implementation, run:

    ```bash
    python app.py
    ```

   For Streamlit implementation, run:

    ```bash
    python app-streamlit.py
    ```

3. Open the provided interface URL in your web browser.

4. Upload your meeting transcript `.docx` file.

5. The AI agents will process the transcript, and the generated BRD will be displayed in markdown format.

## Agent Details
- **Business Analyst Agent**:
  - **Role**: Effectively translate meeting transcripts and discussions into a well-structured BRD.
  - **Goal**: Accurately capture project requirements and stakeholder needs.
  - **Tools**: Includes File Read Tool and Semantic Search Tool.
  - **Backstory**: Experienced in business analysis with a strong understanding of technical environments and documentation.
- **Subject Matter Expert (SME) Agent**:
  - **Role**: Ensure technical feasibility and translate technical discussions into actionable requirements.
  - **Goal**: Propose a clear and concise project name and ensure technical accuracy in the BRD.
  - **Tools**: File Read Tool and Semantic Search Tool.
  - **Backstory**: Possesses in-depth knowledge in the project's domain, crucial for refining technical aspects of the BRD.
## Crew and Task Configuration
- **Crew Configuration**:
  - Composed of a Business Analyst and a Subject Matter Expert.
  - Uses a hierarchical management approach to process tasks effectively.
  - **Manager LLM**: Utilizes the ChatOpenAI model GPT-3.5 Turbo, configured with a zero temperature setting for deterministic responses, enhancing the crew's decision-making processes.
- **Task Definitions**:
  - **Analyze Meeting for BRD Task**: Involves extracting and organizing information from meeting transcripts into the BRD template.
  - **SME Technical Review Task**: Reviews and refines the technical content within the BRD, ensuring all functionalities are realistic and feasible.

## File Structure

- `app.py`: Main application file containing the Gradio interface and processing logic.
- `app-streamlit.py`: Alternative main application file containing the Streamlit interface for similar functionality.
- `brd-template/`: Directory containing the BRD template in markdown format.
- `meeting-transcription/`: Directory where processed meeting transcripts will be saved.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment file for storing sensitive information like API keys.

## Code Explanation

### Main Components

- **Agent Definition**: Defines the roles and goals of the Business Analyst and SME agents.
- **Task Definition**: Specifies the tasks for each agent, including detailed instructions on how to process the meeting transcript and fill out the BRD template.
- **Crew Configuration**: Configures the agents and tasks within a hierarchical management process.
- **File Processing**: Handles the upload and conversion of meeting transcripts from `.docx` to markdown format.
- **Gradio Interface**: Provides a user-friendly web interface for uploading files and displaying results.

### Key Functions

- `call_crew_kickoff(str_current_datetime)`: Initializes and runs the CrewAI agents to process the meeting transcript and generate the BRD.
- `process_file(input_file)`: Handles file upload, conversion, and invokes the `call_crew_kickoff` function to process the transcript.
- `demo.launch()`: Launches the Gradio interface.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [CrewAI](https://crew.ai/) for providing the AI agent framework.
- [Gradio](https://gradio.app/) for the user interface components.
- [Mammoth](https://github.com/mwilliamson/mammoth) for the .docx to markdown conversion.

## Reference URLs
- [Hugging Face Deployed Model](https://huggingface.co/spaces/rawahabinkhalid/Gen-AI-Powered-Documentation-Specialist) for the deployed machine learning model.
- [GitHub Repository](https://github.com/rawahabinkhalid/Gen-AI-Powered-Documentation-Specialist) for the project's repository.

## Contact

For any inquiries or feedback, please contact [rawahabinkhalid@gmail.com](mailto:rawahabinkhalid@gmail.com).