from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hopeful-timing-460610-c6-394d9f1c4714.json"

class YearCountView(APIView):
    def get(self, request):
        client = bigquery.Client()
        query = """
            SELECT release_year, count
            FROM `hopeful-timing-460610-c6.netflix_etl.year_counts`
            ORDER BY release_year
        """

        result = client.query(query).result()
        data = [dict(row)for row in result]
        return Response(data)