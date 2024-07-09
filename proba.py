import datetime
import os
from docx import Document

# Set the environment variable if not already set
os.environ['GROQ_API_KEY'] = os.environ.get('GROQ_API_KEY', "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")

# Check if the environment variable is correctly set
print("GROQ_API_KEY:", os.environ.get("GROQ_API_KEY"))

from groq import Groq

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
    print(completion.choices[0].message.content)

    # Save the completion result to a file
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_file_name = f"rezumat_oferta_1_1.txt"
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(completion.choices[0].message.content)
else:
    print("Structură de răspuns neașteptată:", completion)
#Partea buna 