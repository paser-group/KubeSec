[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Actions Status](https://github.com/paser-group/KubeSec/workflows/Build%20KubeTaint/badge.svg)](https://github.com/Build%20TaintPupp/actions)


# Taintube: Taint Tracking for Security Analysis of Kubernetes Manifests 

## Development Environment
We use Conda to manage the virtual environment for KubeSec. To see the content of the environment, see [environment.yml](./environment.yml). The tool uses [`yq`](https://github.com/mikefarah/yq) as a pre-requisite. 

To use the environment, use the following commands.

```bash
# Create a new environment called KUBESEC if it does not exist
conda env create -f environment.yml

# Activate the KUBESEC enviroment
conda activate KUBESEC

# Deactivate
conda deactivate

# Export (if you modify the environment)
conda env export --from-history > environment.yml
```

## Running the tool

The tool is available as a Docker image: https://hub.docker.com/repository/docker/akondrahman/sli-kube 

### Instruction to run SLI-KUBE from Docker Hub:

- docker rm $(docker ps -a -f status=exited -f status=created -q)
- docker rmi -f $(docker images -a -q)
- docker pull akondrahman/sli-kube
- docker images -a
- docker run --rm -it akondrahman/sli-kube bash
- cd SLI-KUBE-WORK/KubeSec-master/
- python3 main.py

### Instruction to Build and run SLI-KUBE locally

You can build the docker container locally. 

To run the tool, first clone the repository
```bash
git clone https://github.com/paser-group/KubeSec
```

Go to the project directory
```bash
cd KubeSec
```

Switch to `update-readme` branch
```bash
git checkout update-readme
```


Run the following command to build the docker image and run the container.

```bash

git clone 

# Build the image
docker build -t slikube .

# Run the container, volume map the repository path (absolute path) to /iac.
# For example, if the repository you want to scan is at `/Users/john/Desktop/repo1`, then
# use the following Docker run command:
docker run --rm -v /Users/john/Desktop/repo1:/iac --name slikube slikube /iac
```

After running the tool, you will find a CSV file called 'slikube_results.csv' and a SARIF file called 'slikube_results.sarif' in the scanned directory.

## Collaborators 

Akond Rahman (Lead), Rahul Pandita, and Shazibul Islam Shamim 


