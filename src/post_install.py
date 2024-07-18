import subprocess
import spacy

def download_spacy_model():
    # Check if 'en_core_web_sm' model is already installed
    try:
        spacy.load('en_core_web_sm')
        print("en_core_web_sm is already installed.")
    except OSError:
        # If not installed, download the model
        subprocess.run(['python', '-m', 'spacy', 'download', 'en_core_web_sm'], check=True)
        print("en_core_web_sm has been downloaded and installed.")

if __name__ == "__main__":
    download_spacy_model()
