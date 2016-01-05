from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from subprocess import check_output

from .models import Sample
from .label_literals import get_literal_by_label


class RecognizeEquation(APIView):
    """
    Implements the API call for recognizing an equation
    """

    # Recognizes the provided equation and returns the result.
    def post(self, request, format=None):
        # Get the data send by the request.
        inkml_data = request.data.get('inkml_data', '')

        response = check_output([
            "java "
            "-cp /var/www/production/handwritten_equation_recognizer-0.9.jar:"
            "/var/www/production/neural_network-0.9.jar "
            "org.hwer.executables.HandWrittenEquationRecognizer "
            "\"/var/www/production/main-4096-100-100-100-18.bin\" " +
            "\"" + inkml_data + "\""],
            shell=True)

        return Response(response, status=status.HTTP_200_OK)


class Sample(APIView):
    """
    Implements the API call for saving an equation on the database
    """

    def post(self, request, format=None):
        # Get the data send by the request.
        inkml_data = request.data.get('inkml_data', '')
        label = request.data.get('label', '')

        # If any of the data are void, do nothing.
        if inkml_data == '' or label == '':
            return Response("empty data", status=status.HTTP_400_BAD_REQUEST)

        Sample.objects.create(xml=inkml_data, label=label,
                              label_literal=get_literal_by_label(label))

        return Response("successfully saved sample", status=status.HTTP_200_OK)
