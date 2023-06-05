FROM continuumio/miniconda3

WORKDIR /app

RUN conda config --append channels conda-forge

# Create the environment:
COPY environment.yml .
RUN conda env create -v -f environment.yml

# Make RUN commands use the new environment:
RUN echo "conda activate KUBESEC" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]
ENV PATH /opt/conda/envs/KUBESEC/bin:$PATH

# The code to run when container is started:
COPY constants.py graphtaint.py main.py parser.py scanner.py /app/
ENTRYPOINT ["python", "/app/main.py"]