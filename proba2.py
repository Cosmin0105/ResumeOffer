import datetime
import os
from docx import Document
from groq import Groq

# Set the environment variable if not already set
os.environ['GROQ_API_KEY'] = os.environ.get('GROQ_API_KEY', "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")

# Check if the environment variable is correctly set
print("GROQ_API_KEY:", os.environ.get("GROQ_API_KEY"))

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Function to extract text from a .docx file
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


# Function to validate the offer
def validate_offer(offer_text):
    # Validează structura ofertei
    required_sections = [
        "Descrierea aplicației solicitate",
        "Tehnologiile folosite pentru dezvoltarea aplicației",
        "Task-urile concrete și detaliate necesare pentru dezvoltarea aplicației"
    ]
    missing_sections = [section for section in required_sections if section not in offer_text]
    if missing_sections:
        return False, f"Missing sections: {', '.join(missing_sections)}"
    return True, "Offer is valid"


# Read content from the .docx file
job_offer_content = read_docx('Oferta - Test 1.docx')

# Create a completion request for the job offer
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": (
                "Textul următor este în limba română. "
                "Te rog să construiești un rezumat personalizat pentru această ofertă de job. "
                "Extrage următoarele informații: "
                "■ Descrierea aplicației solicitate.\n"
                "■ Tehnologiile folosite pentru dezvoltarea aplicației (ex: stack tehnologic - front-end, back-end, baze de date, etc.).\n"
                "■ Task-urile concrete și detaliate necesare pentru dezvoltarea aplicației, "
                "inclusiv cele care nu sunt menționate direct de client dar sunt necesare (ex: secțiuni financiare, facturare, etc.).\n\n"
                f"Aici sunt detaliile:\n{job_offer_content}"
            )
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

# Check if the completion response has the expected structure
if hasattr(completion, 'choices') and completion.choices:
    # Print the completion result
    offer_text = completion.choices[0].message.content
    print("Offer text:\n", offer_text)

    # Validate the offer
    is_valid, validation_message = validate_offer(offer_text)
    if is_valid:
        print("Oferta este validă.")
        # Save the completion result to a file
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_file_name = f"rezumat_oferta_2_{timestamp}.md"
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(offer_text)
        print(f"Offer saved successfully as {output_file_name}")
    else:
        print("Oferta nu este validă:", validation_message)
else:
    print("Structură de răspuns neașteptată:", completion)
