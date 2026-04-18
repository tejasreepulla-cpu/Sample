from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader("C:\\PythonLife\\project\\looping_statements.pdf")
content=""
for page in reader.pages:
    text=page.extract_text()
    if text:
        content += text + " "
        

tts = gTTS(text=content, lang='en')
tts.save('eaudiofile.mp3')