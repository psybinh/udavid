# CI/CD, Github & Code Quality

1. The project demonstrates an understanding of CI and Github.
All project code is stored in a GitHub repository and a link to the repository has been provided for reviewers. The student uses a CI tool to build the application

github: https://github.com/psybinh/udavid

2. The project has a proper documentation.
The README file includes introduction how to setup and deploy the project. It explains the main building blocks and has comments in the important files

README: https://github.com/psybinh/udavid/blob/master/README.md

3. The project use continuous deployments (CD)
A CD tool is in place to deploy new version of the app automatically to production. The way is described and easy to follow

<!-- Circle CI screenshot: -->

# Container

1. The app is containerized
There is a Dockerfile in repo and the docker image can be build

frontent Dockerfile: https://github.com/psybinh/udavid/blob/master/frontend/Dockerfile
backend Dockerfile: https://github.com/psybinh/udavid/blob/master/backend/Dockerfile

2. The project have public docker images
On DockerHub images for the application are available

<!-- Docker hub screenshot: -->

3. The applications runs in a container without errors
Starting the app as a container on a local system

`docker-compose.yml` file: https://github.com/psybinh/udavid/blob/master/docker-compose.yml

<!-- `docker-compose up` screenshot on the local: -->

<!-- Website screenshots: -->



# Deployment

1. The application runs on a cluster in the cloud
The project can be deployed to a kubernetes cluster

<!-- `kubectl get deployments` screenshot: -->

<!-- `kubectl get pods` screenshot: -->

<!-- `kubectl get services` screenshot: -->

<!-- Website URL: -->

<!-- Website screenshots: -->

2. The app can be upgraded via rolling-update
The students can deploy a new version of the application without downtime 

<!-- Add Yolo model `yolov7-tiny_736x1280.onnx` to S3 -->

<!-- Edit backend Dockerfile:  -->

<!-- Edit fronend code:  -->

<!-- Edit backend code: -->

<!-- Re-build fronend docker: -->

<!-- Re-build backend docker: -->

3. A/B deployment of the application
Two versions of the same app can run at the same and service traffic

<!-- ??? -->

4. Monitoring
The application is monitored by Amazon CloudWatch

<!-- CloudWatch screenshot: -->
