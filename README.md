🩺 Intelligent Medical Diagnosis System
Welcome to the Intelligent Medical Diagnosis System, an AI-powered web application built with Python and Gradio that provides treatment suggestions based on patient symptoms. The system leverages an OWL ontology (HealthcareOntology.xml) for structured healthcare data and a predefined dataset of symptoms and treatments.
📖 Overview
This project is a user-friendly medical diagnosis tool designed to:

Accept a patient's name and symptom via a modern Gradio interface.
Suggest treatments based on a comprehensive dataset of 20+ symptoms.
Utilize an OWL ontology to structure healthcare-related concepts (e.g., Patient, Disease, Treatment).
Provide a clean, professional UI with custom CSS styling.

Disclaimer: This tool is for educational purposes only and is not a substitute for professional medical advice. Always consult a healthcare provider for accurate diagnosis and treatment.
🛠️ Features

Interactive UI: Built with Gradio Blocks for a responsive and intuitive experience.
Extensive Symptom List: Covers 20+ conditions, including flu, diabetes, anxiety, and more.
Ontology Integration: Uses owlready2 to load and interact with the HealthcareOntology.xml file.
Custom Styling: Modern design with a gradient background, rounded buttons, and clear typography.
Clear Functionality: Includes a "Clear Inputs" button for improved user experience.


📋 Prerequisites
To run this project locally, ensure you have the following installed:

Python 3.8+
Required Python packages (see Installation)
A web browser for accessing the Gradio interface



Create a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Install the required Python packages using pip:
pip install gradio owlready2


Ensure Ontology File:Place the HealthcareOntology.xml file in the project root directory. This file defines the ontology structure for healthcare concepts.


🚀 Usage

Run the Application:Execute the Python script to launch the Gradio interface:
python medical_diagnosis_app.py


Interact with the System:

Enter a patient's name in the "Patient Name" field.
Select a symptom from the dropdown menu (e.g., "flu", "migraine").
Click the Diagnose Now button to view the diagnosis and treatment suggestions.
Use the Clear Inputs button to reset the form.


View Results:

The diagnosis, patient name, and recommended treatments will appear in the output box.
Copy the results using the copy button if needed.



📂 Project Structure
medical-diagnosis-system/
├── HealthcareOntology.xml    # OWL ontology file for healthcare concepts
├── medical_diagnosis_app.py  # Main Python script with Gradio UI and logic
├── README.md                # This file

🧬 Ontology Details
The HealthcareOntology.xml file defines a lightweight OWL ontology with classes such as:

Person, Patient, Doctor, Nurse
Treatment, Medication, Surgery
Diagnosis, Disease
Hospital, Department, MedicalRecord

This ontology is loaded using the owlready2 library and can be extended to support more complex healthcare relationships in future iterations.
🩹 Supported Symptoms
The system currently supports the following symptoms and their treatments:

Flu
COVID
Cold
Asthma
Diabetes
Migraine
Anxiety
Depression
Pneumonia
Allergy
Hypertension
Fever
Fracture
Arthritis
Gastritis
Urinary Tract Infection
Conjunctivitis
Sprain
Sinusitis
Insomnia
...and more!

Each symptom is mapped to a list of 3–4 treatment recommendations, such as medications, lifestyle changes, or therapies.





