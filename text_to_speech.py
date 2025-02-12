from gtts import gTTS

def text_to_speech(input_txt_file, output_audio_file="output.mp3", lang="es"):
    try:
        # Leer el archivo de texto
        with open(input_txt_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Convertir el texto a voz
        tts = gTTS(text=text, lang=lang, slow=False)

        # Guardar el archivo de audio
        tts.save(output_audio_file)
        print(f"Audio guardado como {output_audio_file}")

    except Exception as e:
        print(f"Error: {e}")

text_to_speech("archivo.txt")
