[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Actions Status](https://github.com/paser-group/KubeSec/workflows/Build%20KubeTaint/badge.svg)](https://github.com/Build%20TaintPupp/actions)


# Taintube: Taint Tracking for Security Analysis of Kubernetes Manifests 

## Development Environment
We use Conda to manage the virtual environment for KubeSec. To see the content of the environment, see [environment.yml](./environment.yml).

To use the environment, use the following commands.

```bash
# Create
conda env create -f environment.yml

# Activate
conda activate KUBESEC

# Deactivate
conda deactivate

# Export (if you modify the environment)
conda env export --from-history > environment.yml
```

## Running the tool

The tool is available as a Docker image: https://hub.docker.com/repository/docker/akondrahman/sli-kube 

### Instruction to run the tool from Docker Hub:

- docker rm $(docker ps -a -f status=exited -f status=created -q)
- docker rmi -f $(docker images -a -q)
- docker pull akondrahman/sli-kube
- docker images -a
- docker run --rm -it akondrahman/sli-kube bash
- cd SLI-KUBE-WORK/KubeSec-master/
- python3 main.py

### Build and run locally
You can also build the docker container locally.

After running the tool, you will find a CSV file called 'slikube_results.csv' in the scanned directory.

```bash
# Build the image
docker build -t slikube .

# Run the container 
# Replace '/Users/phu/Desktop/tf-open-source/aws-eks-base' with your local path
docker run --rm -v /Users/phu/Desktop/tf-open-source/aws-eks-base:/iac --name slikube slikube /iac
```

## Collaborators 

Akond Rahman (Lead), Rahul Pandita, and Shazibul Islam Shamim 


