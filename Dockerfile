FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir requests schedule 

# Set environment variables
ENV GITHUB_USERNAME="SireJeff"\
    GITHUB_TOKEN="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"\
    REPO_OWNER="SireJeff"\
    REPO_NAME="web_api_sales"\
    FILE_PATH="./test.txt"

CMD ["python", "main.py"]
