# Text Summarizer

### Project Overview

The Text Summarizer is a web application designed to summarize long pieces of text into concise summaries. Utilizing natural language processing techniques, it aims to provide a quick and efficient way to understand the main points of large bodies of text. This project leverages Flask for the web framework and various Python libraries for text processing and summarization.

### Model Used: spaCy
The Text Summarizer uses the spaCy library, a powerful and efficient natural language processing library in Python. spaCy provides pre-trained models for a variety of languages and tasks, including named entity recognition, part-of-speech tagging, and dependency parsing. In this project, spaCy is utilized for its robust text processing capabilities to generate accurate and meaningful summaries.

### How spaCy is Used in This Project

* Text Preprocessing: spaCy is used to tokenize the input text, ensuring that sentences and words are accurately identified.
* Named Entity Recognition: Identifies key entities within the text, which can be crucial for generating contextually relevant summaries.
* Dependency Parsing: Understands the grammatical structure of sentences to maintain the meaning and coherence in the summarized text.

### Features

* Text Summarization: Automatically generates summaries from input text.

* Interactive UI: User-friendly interface to input text and view summaries.

* Responsive Design: Ensures compatibility across different devices and screen sizes.

* Background Customization: Uses a custom background image for the web interface.

### Project Structure

The project is organized into the following directories and files:

* src/: Contains the main Python scripts for text summarization, including text_summary.py for processing and summarizing text, post_install.py for post-installation tasks, and __init__.py to initialize the module.

* requirements.txt: Lists the required Python packages.

* application.py: The main Flask application script.

* setup.py: Script for setting up the project environment.

* static/: Contains static files like CSS and background images, including style.css for the web application’s styles and paper.jpg for the background image.

* templates/: HTML templates for the web application, including index.html for the main page and summary.html for displaying the summarized text.

### Installation

* To install the project, follow these steps:

* Clone the repository from GitHub.
  -> git clone https://github.com/mohdmojammil3/Text-Summarizer.git

* Create a virtual environment.
  -> conda create -p venv python==3.11.7 -y

* Activate the virtual environment
  -> conda activate "your venv path"  or -> conda activate venv

* Install the required packages listed in requirements.txt.
  -> pip install -r requirements.txt
* Run the application using the Flask development server.
  -> python application.py

* Open the application in your web browser.

### Usage

To use the Text Summarizer:

* Navigate to the application URL in your web browser.
* Enter the text you want to summarize in the text area.
* Click the 'Summarize' button to generate the summary.
* View the summarized text in the summary box.

### Customization

You can customize the background image by replacing static/paper.jpg with your own image. To change the styling of the web application, modify static/style.css.

### Example Output

The application provides an output displaying the original length, summary length, and the summary itself. Here is an example:

Original Length: 131
Summary Length: 25
Summary: "Since Bitcoin's introduction in 2009, blockchain uses have exploded via the creation of various cryptocurrencies, decentralized finance (DeFi) applications, non-fungible tokens (NFTs), and smart contracts."
Contributing
If you’d like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch.
Make your changes and commit them.
Push to your branch.
Create a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any questions or suggestions, please feel free to contact [Er. Md. Mojammil] at [mohdmojammil3@gmail.com].