# ResumeOffer

    Această aplicație Python utilizează API-ul Groq (llama3-70b-8192) pentru a genera automat rezumate personalizate pentru oferte de job extrase din documente .docx. Utilizatorul poate introduce numele fișierului .docx și numărul documentului pentru a extrage și sintetiza informațiile cheie necesare pentru o evaluare rapidă a ofertei de job.

Pași pentru utilizare:
1. Obținerea cheii API Groq:
   Accesează https://console.groq.com/keys pentru a genera o cheie API.
2. Setarea cheii API:
   După ce ai obținut cheia API, utilizează următoarea comandă în terminal pentru a seta cheia API:

        export GROQ_API_KEY=cheia_ta_generată

    Această comandă este crucială pentru a asigura că scriptul are acces corect la API-ul Groq.
   
3. Selectarea modelului Groq:
    Pentru rezolvarea problemei tale, selectează modelul:
   
    Model: llama3-70b-8192
   
4. Instalarea pachetelor Python necesare:
   
Instalează pachetele python-docx și groq folosind următoarele comenzi:

        pip install python-docx
  ![image](https://github.com/Cosmin0105/ResumeOffer/assets/120392090/8b978f92-7ef8-4a20-9f23-60ce9e16fc86)
  
        pip install groq
  ![image](https://github.com/Cosmin0105/ResumeOffer/assets/120392090/f3d75d25-7346-467e-9255-ed5b5b8d17ce)
      

5. Utilizarea scriptului:

    Rulează scriptul cu numele main.py și urmează instrucțiunile pentru a introduce numele fișierului .docx, numărul documentului și numele dorit pentru fișierul de ieșire.
    Scriptul va extrage conținutul din documentul .docx, va genera automat un rezumat personalizat folosind API-ul Groq și va salva rezumatul într-un fișier text cu numele specificat.

Funcționalitatea proiectului

    Extragerea conținutului din fișierul .docx: Scriptul extrage textul integral dintr-un fișier .docx specificat de utilizator.

    Generarea rezumatului personalizat: Folosind API-ul Groq (Llama), scriptul creează o solicitare de completare pentru a genera un rezumat personalizat al informațiilor cheie din ofertă. Acest rezumat include detalii precum descrierea aplicației, tehnologiile utilizate și task-urile necesare pentru dezvoltare.

    Salvarea rezumatului într-un fișier .txt: Rezumatul generat este salvat automat într-un fișier .txt cu numele specificat de utilizator, fără extensie.


Exemplu de utilizare

    Utilizatorii trebuie sa ruleze main.py pentru  a introduce numele fișierului .docx (de exemplu, Oferta - Test 1.docx), numărul documentului și numele dorit pentru fișierul de ieșire (de exemplu, rezumat_oferta_1). Scriptul extrage informațiile cheie din document, apelează API-ul Groq pentru a genera un rezumat, și salvează rezumatul într-un fișier text cu numele specificat.
    
![image](https://github.com/Cosmin0105/ResumeOffer/assets/120392090/9815dd30-737a-42d3-8fac-79c450f76ef9)



![WhatsApp Image 2024-07-09 at 15 55 19_b27ac32c](https://github.com/Cosmin0105/ResumeOffer/assets/120392090/e219a57c-c908-49aa-b390-39fd38fe6e3a)



