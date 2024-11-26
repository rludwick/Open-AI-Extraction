from pdf2image import convert_from_bytes
import openai
import io
import base64
from dotenv import load_dotenv
import os
import json

# Function to encode the PDF image.
def encodeImage(image):

    # Save the image to a bytes buffer in JPEG format.
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    
    # Encode the image in base64.
    return base64.b64encode(buffer.read()).decode('utf-8')

def processPDF(file):

    # Load environment variables from a .env file.
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Convert PDF pages to images.
    images = convert_from_bytes(file.read())

    # Encode all images to base64 and prepare for the OpenAI request.
    base64Images = [encodeImage(image) for image in images]
    
    # Prepare messages with the prompt.
    messages = [
        {
            "role": "user",
            "content": [
                "The following images represent pages from a PDF document. "
                "Review all pages collectively and extract the following structured information:\n"
                "1. Account owner name\n"
                "2. Portfolio value\n"
                "3. Name and cost basis of each holding\n\n"
                "Respond only with JSON."
            ],
        }
    ]

    # Loop through base64 images and append each one to the messages.
    for base64Image in base64Images:
        messages[0]["content"].append(
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64Image}",
                    "detail": "low"
                },
            }
        )

    # Send the request to OpenAI.
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # Extract the content from the response.
    if hasattr(response, 'choices') and len(response.choices) > 0:
        content = response.choices[0].message.content
        
        # Parse the JSON content.
        try:
            json_data = json.loads(content.strip('```json').strip('```').strip())
            return json_data
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON."}
    else:
        return {"error": "No valid content extracted."}