FROM python:3.12


WORKDIR /workspace
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install poetry uv
COPY pyproject.toml poetry.lock ./
RUN poetry install -e .
COPY . .
ENTRYPOINT ["sugar-mcp"]
