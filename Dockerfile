FROM python:3.12

WORKDIR /workspace
COPY . .
RUN pip install .
ENTRYPOINT ["sugar-mcp"]
