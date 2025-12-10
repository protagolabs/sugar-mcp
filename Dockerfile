FROM python:3.12


WORKDIR /workspace
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .
RUN pip install .
ENTRYPOINT ["sugar-mcp"]
