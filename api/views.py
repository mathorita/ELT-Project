from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from google.cloud import bigquery
import os

import json
from google.cloud import bigquery
from google.oauth2 import service_account

credentials_info = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])
credentials = service_account.Credentials.from_service_account_info(credentials_info)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

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