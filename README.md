# Roll Dice API - Kubernetes Deployment Example

This repository is a part of a Master's in Data Engineering practical activity. It contains an example FastAPI application that simulates dice rolls, which can be containerized and deployed on a Kubernetes cluster. The application is designed to be run in a local development environment using Docker Desktop with Kubernetes enabled.

## Repository Structure

- `/app`: Contains the FastAPI application source code.
- `/kubernetes`: Includes the Kubernetes YAML configuration files for setting up the deployment and service.
- `/assets`: Stores all the commands used and screenshots taken during the setup and deployment process.

## Docker Image

The Docker image for the API is available on Docker Hub and can be pulled using the following command:

```
docker pull jrvm/m2-actividad3.1:1.0
```


## Prerequisites

- Docker Desktop with Kubernetes enabled
- kubectl CLI tool installed and configured
- Access to Docker Hub for pulling the image

## Getting Started

To get started with deploying the Roll Dice API to your local Kubernetes cluster, follow these steps:

1. Clone the repository to your local machine:

```shell
[git clone https://github.com/your-github-username/your-repo-name.git](https://github.com/Rafavermar/FastAPI-K8S-Simple-Exercise.git)
```

2. Navigate to the kubernetes directory:
```
cd your-repo-name/kubernetes
```
3. Apply the Kubernetes configurations:
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

4. Once the deployment is up and running, find the NodePort assigned to the service:
```
kubectl get svc -n virtualizacion
```
5. Access the API by making a GET request to the NodePort. For example:
 Replace NodePort with the actual port number displayed from the previous command.

```
curl "http://localhost:NodePort/dice?amount=2&sides=6"
```
6. To access the Swagger UI, navigate to:
```
http://localhost:NodePort/docs
```

Troubleshooting
If you encounter any issues with deploying the application, you can refer to the commands in the /assets directory for guidance or rollback steps.

Contribution
Contributions to the repository are welcome. Please ensure that you test the changes in your local environment before making a pull request.

### Acknowledgments
I'd like to express my sincere gratitude to our teacher @MANUEL ENRIQUE GOMEZ MONTERO whose ability to convey complex information with clarity made our learning about Virtualization boost!

