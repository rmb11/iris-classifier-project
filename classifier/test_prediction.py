import json
from django.test import TestCase, Client
from django.urls import reverse

from ml.predict import predict 

class PredictFunctionTests(TestCase):
    def test_predict_returns_valid_species(self):
        """
        This test checks that the predict() function
        gives back one of the three iris flower names.
        """
         # Example iris measurements for a sample flower.
        result = predict(5.1, 3.5, 1.4, 0.2)

        # Make sure the result is one of the expected labels.
        self.assertIn(result, ["setosa", "versicolor", "virginica"])
        
    def test_predict_with_different_values_is_still_valid(self):
        """
        This test uses a different set of iris measurements
        and still makes sure the result is a valid species name.
        """
        result = predict(6.2, 2.8, 4.8, 1.8)
        self.assertIn(result, ["setosa", "versicolor", "virginica"])


class PredictApiBasicTests(TestCase):
    def setUp(self):
        # This creates a fake browser we can use to call our API.
        self.client = Client()

    def test_predict_api_returns_200(self):
        """
        This test checks that our prediction API is working.
        We send it some example iris data and make sure the
        response comes back with a 200 OK status code.
        """
        # Look up the URL for the predict API from urls.py.
        url = reverse("predict_api")

        # These are example iris measurements.
        payload = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        }

        # Send a POST request with JSON data.
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type="application/json",
        )

        # The API should return 200 OK if everything works.
        self.assertEqual(response.status_code, 200)