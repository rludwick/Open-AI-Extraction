from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .utils import processPDF
from rest_framework.parsers import MultiPartParser

class ExtractInfoAPIView(APIView):
    """
    This class defines an API endpoint to:

    Accept a PDF file uploaded by a client.
    Process the PDF and extract structured information via OpenAI Vision.
    Return the extracted information as a JSON response.
    """

    # Specifies that this API expects file uploads in the request body.
    parser_classes = [MultiPartParser]

    # Handles HTTP POST requests.
    def post(self, request, *args, **kwargs):

        # Extracts the uploaded file from the request data.
        file = request.data.get('file', None)
        if not file:
            return Response({"error": "No file uploaded"}, status=400)
        
        if not file.name.endswith('.pdf'):
            return Response({"error": "Invalid file type. Only PDF files are allowed."}, status=400)

        try:
            # Process the PDF with OpenAI Vision.
            extractedInfo = processPDF(file)
        except Exception as e:
            return Response({"error": f"Error processing PDF: {str(e)}"}, status=500)

        # Sends a success response containing the extracted structured information as a JSON.
        return Response({"data": extractedInfo})