#syntax=docker/dockerfile:1.4
FROM public.ecr.aws/docker/library/python:3.11.9-slim

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Set environment variables
# ENV COGNITO_DOMAIN='<COGNITO_DOMAIN>'
# ENV REGION='us-east-1'
# ENV USER_POOL_ID='<USER_POOL_ID>'
# ENV CLIENT_ID='<CLIENT_ID>'
# ENV CLIENT_SECRET='<CLIENT_SECRET>'
# ENV IDENTITY_POOL_ID='<IDENTITY_POOL_ID>'
# ENV AUTHENTICATED_ROLE_ARN='<AUTHENTICATED_ROLE_ARN>'
# ENV GRAPHQL_ENDPOINT='<GRAPHQL_ENDPOINT>'
# ENV S3_INPUT_BUCKET='<S3_INPUT_BUCKET>'
# ENV S3_PROCESSED_BUCKET='<S3_PROCESSED_BUCKET>'
# ENV CLIENT_NAME='<CLIENT_NAME>'
# ENV APP_URI='http://localhost:8501'

ENV COGNITO_DOMAIN="https://2c260970-773f-11ef-b100-120b7ff7118d.auth.us-east-1.amazoncognito.com"
ENV REGION='us-east-1'
ENV USER_POOL_ID="us-east-1_90RLlUG2T"
ENV CLIENT_ID="1d6il0cip2ols4g0cisn0rj9e6"
ENV CLIENT_SECRET="13v4i63sccjb8eu4tok9jrr7upg9kg914m0thtobueriqtv5h9qu"
ENV IDENTITY_POOL_ID="us-east-1:6979f202-feee-45dd-bc3c-512672b7eeac"
ENV AUTHENTICATED_ROLE_ARN="arn:aws:iam::059314543988:role/ApiStack-CognitoAuthenticatedRole5CA1BC89-mJJdzyxlimWa"
ENV GRAPHQL_ENDPOINT="https://j3tc7xl4mndnvbcryjjot7u3l4.appsync-api.us-east-1.amazonaws.com/graphql"
ENV S3_INPUT_BUCKET="persistencestack-inputassets7d1d3f52-fort2byibjlz"
ENV S3_PROCESSED_BUCKET="persistencestack-processedassets6ba25f4c-fwg13jwuqc8r"
ENV CLIENT_NAME='agents'
ENV APP_URI="http://localhost:8501/"
EXPOSE 8501
COPY . .
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501"]



