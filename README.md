# mnist serving example
mnist serving example using Tensorflow 2.0 & flask

### install libraries
```
pip3 install -r requirements.txt
```

### train
Training mnist with simple network and save as a saved model format
```
python3 train.py
```

### serving using flask
serving your model using flask
```
python3 flask_server.py #if you want to execute at background: nohup python3 flask_server.py &
```

### serving using flask with swagger
serving your model using flask with swagger
swagger page: 127.0.0.1:2431
```
python3 flask_server_swagger.py 
```

### serving using flask with gunicorn
```
gunicorn flask_server:app -b 0.0.0.0:2431 -w 4
gunicorn flask_server_swagger:app -b 0.0.0.0:2431 -w 4
```

### test
You can test rest api.
```
python3 flask_test.py
```

<br>
https://seokhyun2.tistory.com/40
