# deploy
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml

kubectl apply -f backend-service.yaml
kubectl apply -f frontend-service.yaml

kubectl expose deployment udavid-frontend --type=LoadBalancer --name=publicfrontend

kubectl get services

# delete all
kubectl delete deployments udavid-backend udavid-frontend
kubectl delete services udavid-backend udavid-frontend publicfrontend