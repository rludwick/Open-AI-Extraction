# Investment Statement Parser - OpenAI Vision Integration.

## Overview
Tool designed to extract structured financial information from investment statement PDFs. It utilizes **OpenAI's Vision model** to process PDF documents, converting them to images, and then extracting key data such as account owner names, portfolio values, and holdings.

## Features
- Extracts account owner names, portfolio values, and cost basis of holdings.
- Supports PDF documents in a variety of formats (through image extraction).
- Uses **OpenAI Vision** to analyze images and extract structured data.
- Scalable and efficient processing for larger PDFs.

## Clone the Repository
Clone this repository to your local machine

## Install Dependencies
Install the necessary Python dependencies:
pip install -r requirements.txt

## Set Up the OpenAI API Key
Make sure you have a valid OpenAI API key. Add it to your .env file:
OPENAI_API_KEY=your-api-key-here

## Start the Django Development Server
python manage.py runserver

## Usage
Send a POST Request to extract information.
Once the server is running, you can send a POST request with a PDF file to the following endpoint:
Endpoint: /api/extract-info/
Method: POST
Body: Upload a PDF file with the key file.

## Expected Response
The response will contain the structured data extracted from the PDF return as a JSON.
