from flask import Flask, request, jsonify, render_template
from src.text_summary import summarizer
import src.post_install

# Ensure the spaCy model is downloaded if not already
src.post_install.download_spacy_model()

application = Flask(__name__)

app = application

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']
        summary, _, original_len, summary_len = summarizer(text)

        # Format the output for display in the template
        output = {
            "Original_length": original_len,
            "Summary_length": summary_len,
            "Summary": summary
        }

        return render_template('index.html', output=output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
