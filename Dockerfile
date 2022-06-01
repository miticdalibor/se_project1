FROM python:3.8-bullseye


RUN pip install poetry
ADD pyproject.toml pyproject.toml
# TODO remove poetry dependencie for python3-dev
RUN poetry install --no-dev
#RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
#RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT [ "streamlit", "run", "streamlit_pizza.py"]
