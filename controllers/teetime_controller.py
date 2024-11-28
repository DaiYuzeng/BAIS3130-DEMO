from flask import Blueprint, request, jsonify
from services.teetime_service import TeeTimes

# Create a Flask blueprint for the TeeTime routes
teetime_controller = Blueprint('teetime_controller', __name__)

@teetime_controller.route('/teetime', methods=['POST'])
def create_teetime():
    data = request.get_json()
    try:
        TeeTimes.create_teetime(data)
        return jsonify({'message': 'Tee Time created successfully.'}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@teetime_controller.route('/teetime/<int:teetime_id>', methods=['GET'])
def get_teetime(teetime_id):
    try:
        teetime = TeeTimes.get_teetime(teetime_id)
        if teetime:
            return jsonify(teetime), 200
        else:
            return jsonify({'error': 'Tee Time not found.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@teetime_controller.route('/teetimes', methods=['GET'])
def find_teetime():
    try:
        teetimes = TeeTimes.find_teetime()
        return jsonify(teetimes), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
