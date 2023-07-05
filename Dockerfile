FROM python:3
RUN git clone /https://github.com/um-computacion-tm/final-2023-07-05-TiagoWeintraub.git
WORKDIR /final-2023-07-05-TiagoWeintraub
CMD ["python3","test_tragamonedas.py"]