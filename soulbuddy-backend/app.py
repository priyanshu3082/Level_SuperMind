from flask import Flask, request, jsonify
from astrapy.client import create_astra_client

app = Flask(__name__)

# Initialize the Astra DB client
client = create_astra_client(
    astra_database_id='e43ad1b3-ac50-408d-ab3d-d06d633c4abc',
    astra_database_region='us-east-2',
    astra_application_token='AstraCS:lMRIZrTYZpzRxhkZSsQImOvF:d7da9fa768dc52c418703cb2bdff2aa5e5b1d3d5011dc2d8f2c686339de0e4b7'
)
collection = client.namespace('your_namespace').collection('user_details')

@app.route('/api/user_details', methods=['POST'])
def add_user_details():
    data = request.json
    try:
        collection.create(data)
        return jsonify({'message': 'Data submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)