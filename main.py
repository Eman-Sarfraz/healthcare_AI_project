import gradio as gr
from owlready2 import *

# Load the ontology (still academic/optional here)
onto = get_ontology("HealthcareOntology.xml").load()

# Expanded treatment dataset with more symptoms and treatments
treatments = {
    "flu": ["medication (antiviral)", "rest", "fluids", "warm compress"],
    "covid": ["antiviral drugs", "oxygen support", "isolation", "monitor symptoms"],
    "cold": ["rest", "fluids", "vitamin C", "nasal decongestants"],
    "asthma": ["inhalers", "bronchodilators", "avoid triggers", "allergy testing"],
    "diabetes": ["insulin therapy", "diet control", "exercise", "blood sugar monitoring"],
    "migraine": ["pain relievers", "rest in a dark room", "hydration", "avoid triggers"],
    "anxiety": ["therapy (CBT)", "meditation", "anti-anxiety meds", "breathing exercises"],
    "depression": ["counseling", "antidepressants", "exercise", "support groups"],
    "pneumonia": ["antibiotics", "oxygen therapy", "hospitalization", "chest physiotherapy"],
    "allergy": ["antihistamines", "avoid allergens", "epinephrine", "allergy shots"],
    "hypertension": ["BP medications", "low-sodium diet", "exercise", "stress management"],
    "fever": ["paracetamol", "hydration", "rest", "cool compress"],
    "fracture": ["immobilization", "cast/splint", "surgery if needed", "physical therapy"],
    "arthritis": ["anti-inflammatory drugs", "physical therapy", "joint protection", "heat/cold therapy"],
    "gastritis": ["antacids", "avoid spicy foods", "proton pump inhibitors", "small meals"],
    "urinary tract infection": ["antibiotics", "hydration", "pain relievers", "avoid irritants"],
    "conjunctivitis": ["antibiotic eye drops", "warm compress", "avoid rubbing eyes", "hygiene"],
    "sprain": ["RICE (Rest, Ice, Compression, Elevation)", "pain relievers", "physical therapy", "bracing"],
    "sinusitis": ["nasal corticosteroids", "decongestants", "hydration", "steam inhalation"],
    "insomnia": ["sleep hygiene", "cognitive behavioral therapy", "melatonin", "avoid caffeine"]
}

def diagnose(name, symptom):
    name = name.lower().strip()
    symptom = symptom.lower().strip()
    response = []

    if symptom in treatments:
        response.append(f"🩺 **Diagnosis:** {symptom.capitalize()}")
        response.append(f"👤 **Patient:** {name.capitalize()}")
        response.append("💊 **Recommended Treatments:**")
        for t in treatments[symptom]:
            response.append(f"• {t.capitalize()}")
        response.append("\n⚠️ **Note:** Consult a healthcare professional for a proper diagnosis and treatment plan.")
    else:
        response.append("❌ No treatment found for this symptom. Please try another symptom or consult a doctor.")

    return "\n".join(response)

# Sort symptoms for dropdown
symptoms_list = sorted(treatments.keys())

# Enhanced Gradio UI using Blocks with modern styling
with gr.Blocks(
    css="""
        .gradio-container {background: linear-gradient(135deg, #e0f7fa, #b2ebf2); font-family: 'Arial', sans-serif;}
        h1 {color: #00796b; text-align: center; font-size: 2.5em; margin-bottom: 10px;}
        .gr-button {background-color: #00796b !important; color: white !important; border-radius: 10px; padding: 10px;}
        .gr-button:hover {background-color: #004d40 !important;}
        .gr-textbox, .gr-dropdown {border-radius: 8px; border: 2px solid #00796b;}
        .gr-textbox label, .gr-dropdown label {color: #00796b; font-weight: bold;}
        .gr-row {gap: 20px;}
        .gr-markdown {color: #004d40;}
        .gr-textbox-output {background-color: #ffffff; border-radius: 10px; padding: 15px; border: 2px solid #00796b;}
    """,
    title="🩺  Medical Diagnosis"
) as demo:
    gr.Markdown(
        """
        # 🩺  Medical Diagnosis System 
        Welcome to the AI-powered medical diagnosis tool made by Eman Sarfraz. Enter the patient's name and select a symptom to receive tailored treatment suggestions.
        """
    )
    
    with gr.Row():
        name_input = gr.Textbox(label="👤 Patient Name", placeholder="Enter patient's name", lines=1)
        symptom_input = gr.Dropdown(choices=symptoms_list, label="🦠 Symptom", value="flu")

    diagnose_btn = gr.Button("🔍 Diagnose Now")
    result_output = gr.Textbox(label="📋 Diagnosis & Treatment Plan", lines=10, show_copy_button=True)

    # Add a clear button for better UX
    clear_btn = gr.Button("🗑️ Clear Inputs")
    clear_btn.click(fn=lambda: ("", None), inputs=None, outputs=[name_input, symptom_input])

    diagnose_btn.click(fn=diagnose, inputs=[name_input, symptom_input], outputs=result_output)

    gr.Markdown(
        """
        ---
        **Disclaimer:** This tool provides general suggestions and is not a substitute for professional medical advice. Always consult a healthcare provider for accurate diagnosis and treatment.
        """
    )

demo.launch()