# python_flask_API
GET data : 
curl http://<IP>:2999/api/endpoint1
POST new data : 
curl -X POST -H "Content-Type: application/json" -d '{KEY:VALUE}' http://<IP>:2999/api/endpoint1
  
docker run -p <host_port>:8080 -e ACCESS_KEY=<access_key> -e SECRET_ACCESS_KEY=<secret_access_key> <image_name>
