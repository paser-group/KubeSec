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

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://github.com/mikefarah/yq/releases/download/v4.33.3/yq_linux_386 -O /usr/bin/yq \ 
    && chmod +x /usr/bin/yq

# The code to run when container is started:
COPY constants.py graphtaint.py main.py parser.py scanner.py /app/
ENTRYPOINT ["python", "/app/main.py"]