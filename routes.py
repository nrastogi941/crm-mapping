from flask import Blueprint, request, jsonify
from database import db
from models import CRMMapping
from serializers import mapping_serializer

mapping_routes = Blueprint('mapping', __name__)

@mapping_routes.route('/mapping', methods=['POST'])
def create_mapping():
    try:
        payload = request.json
        crm_name = payload.get('crm_name')
        mapping = CRMMapping.query.filter_by(crm_name=crm_name).first()
        if mapping:
            return jsonify({'message': 'Mapping already exists for the provider.'}), 400

        new_mapping = CRMMapping(**payload)
        db.session.add(new_mapping)
        db.session.commit()
        return jsonify({'message': 'Mapping created successfully.'}), 201

    except Exception as e:
        return jsonify({'message': 'An error occurred while creating the mapping.', 'error': str(e)}), 500


@mapping_routes.route('/mapping/<crm_name>', methods=['GET'])
def get_mapping(crm_name):
    try:
        mapping = CRMMapping.query.filter_by(crm_name=crm_name).first()
        if not mapping:
            return jsonify({'message': 'Mapping not found.'}), 404
        serializable_mapping = mapping_serializer(mapping)
        return jsonify(serializable_mapping)

    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching the mapping.', 'error': str(e)}), 500


@mapping_routes.route('/mapping/<crm_name>', methods=['PUT'])
def update_mapping(crm_name):
    try:
        mapping = CRMMapping.query.filter_by(crm_name=crm_name).first()
        if not mapping:
            return jsonify({'message': 'Mapping not found.'}), 404

        payload = request.json
        for key, value in payload.items():
            setattr(mapping, key, value)

        db.session.commit()
        return jsonify({'message': 'Mapping updated successfully.'})

    except Exception as e:
        return jsonify({'message': 'An error occurred while updating the mapping.', 'error': str(e)}), 500


@mapping_routes.route('/mapping/<crm_name>', methods=['DELETE'])
def delete_mapping(crm_name):
    try:
        mapping = CRMMapping.query.filter_by(crm_name=crm_name).first()
        if not mapping:
            return jsonify({'message': 'Mapping not found.'}), 404

        db.session.delete(mapping)
        db.session.commit()
        return jsonify({'message': 'Mapping deleted successfully.'})

    except Exception as e:
        return jsonify({'message': 'An error occurred while deleting the mapping.', 'error': str(e)}), 500
