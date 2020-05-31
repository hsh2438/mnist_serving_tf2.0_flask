import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields


load = tf.saved_model.load('mnist/1')
load_inference = load.signatures["serving_default"]


app = Flask(__name__)
api = Api(app, version='1.0', title='mnist classification')
ns  = api.namespace('inference')

mnist_api_model = api.model(name='mnist', model={
    'image': fields.List(fields.List(fields.Float))
})

@ns.route('/')
class InferenceMnist(Resource):
    @api.expect(mnist_api_model)
    def post(self):
        data = request.json['images']
        result = load_inference(tf.constant(data, dtype=tf.float32)/255.0)
        return jsonify(np.argmax(result['dense_1'].numpy()).tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2431)
