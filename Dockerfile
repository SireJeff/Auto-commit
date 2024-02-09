FROM python:3.8-slim

WORKDIR /app

COPY dummy_commit.py .

RUN pip install --no-cache-dir requests schedule

# Set environment variables
ENV GITHUB_USERNAME="your_username" \
    GITHUB_TOKEN="your_personal_access_token" \
    REPO_OWNER="your_repo_owner" \
    REPO_NAME="your_repo_name" \
    FILE_PATH="path/to/your/file.txt"

CMD ["python", "dummy_commit.py"]
