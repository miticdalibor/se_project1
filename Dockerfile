FROM python:3.8-bullseye

WORKDIR /src
RUN pip install poetry
ADD pyproject.toml pyproject.toml
RUN poetry install --no-dev
#RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
#RUN pip install -r requirements.txt

ADD . /src

# ENTRYPOINT [ "streamlit", "run", "ui.py"]
EXPOSE 8080

CMD poetry run streamlit run ui.py
