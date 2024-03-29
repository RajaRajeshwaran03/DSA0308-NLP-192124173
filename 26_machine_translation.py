from transformers import pipeline

def translate_text(text, source_lang='en', target_lang='fr'):
    # Load the pre-trained translation model
    translator = pipeline(f'translation_{source_lang}_to_{target_lang}')
    
    # Translate the input text
    translated_text = translator(text)[0]['translation_text']
    
    return translated_text

# Get input from the user
input_text = input("Enter the English text to translate: ")

# Translate the text from English to French
french_text = translate_text(input_text)

print("Translated text in French:")
print(french_text)
