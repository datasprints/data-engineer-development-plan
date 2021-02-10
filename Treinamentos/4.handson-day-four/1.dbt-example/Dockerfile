FROM python:3.8

COPY profiles.yml /root/.dbt/profiles.yml

WORKDIR /dbt

COPY . /dbt
RUN pip install -r requirements.txt

# install dbt deps
RUN dbt deps