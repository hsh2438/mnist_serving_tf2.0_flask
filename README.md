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
You should have docker to use this example.
```
python3 flask_server.py #if you want to execute at background: nohup python3 flask_server.py &
```

### test
You can test rest api.
```
python3 flask_test.py
```
