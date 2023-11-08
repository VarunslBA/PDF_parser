import PyPDF2
import json
import spacy
def perform_ner(text):
    # Load the English NER model from spaCy
    nlp = spacy.load("en_core_web_sm")
    # Process the text using spaCy
    doc = nlp(text)
    # Extract named entities and their labels
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })
    return entities
def parse_pdf_to_json(pdf_filename, json_filename):
    pdf_text = []
    # Open the PDF file
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Iterate through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text.append(page.extract_text())
    # Process text with NER
    ner_results = [perform_ner(text) for text in pdf_text]
    # Convert the extracted text and NER results to a JSON structure
    pdf_json = {
        'text': pdf_text,
        'ner_results': ner_results
    }
    # Write the JSON to a file
    with open(json_filename, 'w') as json_file:
        json.dump(pdf_json, json_file, indent=4)
if __name__ == "__main__":
    pdf_filename = "test.pdf"  # Change this to your PDF file's path
    json_filename = "output.json"  # Change this to the desired JSON output file
    parse_pdf_to_json(pdf_filename, json_filename)