# CI/CD, Github & Code Quality

### The project demonstrates an understanding of CI and Github.

Circle CI configuration: 

Circle CI screenshot: 

![](./images/CI.png "Circle CI screenshot")

### The project has a proper documentation.

README: https://github.com/psybinh/udavid/blob/master/README.md

### The project use continuous deployments (CD)

Deployment and service files are auto generated from docker-compose.yml using the tool `kompose`

Fontend deployment: https://github.com/psybinh/udavid/blob/master/deploy_eks/frontend-deployment.yaml

Backend deployment: https://github.com/psybinh/udavid/blob/master/deploy_eks/backend-deployment.yaml

Fontend service: https://github.com/psybinh/udavid/blob/master/deploy_eks/frontend-service.yaml

Backend service: https://github.com/psybinh/udavid/blob/master/deploy_eks/backend-service.yaml

# Container

### The app is containerized

frontent Dockerfile: https://github.com/psybinh/udavid/blob/master/frontend/Dockerfile

backend Dockerfile: https://github.com/psybinh/udavid/blob/master/backend/Dockerfile

### The project have public docker images

Docker hub screenshot:

![](./images/docker_hub.png "Docker hub screenshot")

### The applications runs in a container without errors

`docker-compose.yml` file: https://github.com/psybinh/udavid/blob/master/docker-compose.yml

`docker-compose up` screenshot on the local:

![](./images/docker_compose.png "docker-compose up")

Website screenshots:

![](./images/website_local.png "Website screenshots")

# Deployment

### The application runs on a cluster in the cloud

`kubectl get deployments` screenshot:

![](./images/get_deployment.png "Website screenshots")

`kubectl get pods` screenshot:

![](./images/get_pods.png "Website screenshots")

`kubectl get services` screenshot:

![](./images/get_services.png "Website screenshots")

Website URL: http://a6e792be6667d4288a923e90caba9694-530918475.us-east-1.elb.amazonaws.com:8501

Website screenshots:

![](./images/web_eks_1.png "Website screenshots")

![](./images/web_eks_2.png "Website screenshots")

### The app can be upgraded via rolling-update

Edit title of the website

![](./images/edit_title.png "Website screenshots")

rolling-update:

![](./images/re_deploy.png "Website screenshots")

Result after deploy:

![](./images/re_deploy_rs.png "Website screenshots")

### A/B deployment of the application

not yet implemented

### Monitoring

Screenshot `kubectl get pods -n amazon-cloudwatch`:

![](./images/monitor.png "Website screenshots")

Screenshot CloudWatch:

![](./images/cloud_watch.png "Website screenshots")

