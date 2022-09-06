FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

# RUN python -m spacy download en_core_web_sm
 
COPY . .

RUN python3 source.py 

EXPOSE 8501

ENTRYPOINT streamlit run main.py
