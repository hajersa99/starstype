  
import request

url = 'http://localhost:5000/predict_api'
r = request.post(url,json={'x_test'})

print(r.json())