# deploy
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml

kubectl apply -f backend-service.yaml
kubectl apply -f frontend-service.yaml

kubectl expose deployment frontend --type=LoadBalancer --name=publicfrontend

kubectl get services

# delete all
kubectl delete deployments backend frontend
kubectl delete services backend frontend publicfrontend