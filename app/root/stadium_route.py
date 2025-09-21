from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import stadium_controller
from ..domain.stadium import Stadium

stadium_bp = Blueprint('stadium', __name__, url_prefix='/stadium')


@stadium_bp.route('', methods=['GET'])
def get_all_stadiums() -> Response:
    """
    Get all stadiums
    ---
    tags:
      - Stadium
    responses:
      200:
        description: List of all stadiums
        examples:
          application/json: [
            {
              "id": 1,
              "name": "Old Trafford",
              "capacity": 74879,
              "location": "Manchester, UK"
            }
          ]
    """
    return make_response(jsonify(stadium_controller.find_all()), HTTPStatus.OK)


@stadium_bp.route('', methods=['POST'])
def create_stadium() -> Response:
    """
    Create a new stadium
    ---
    tags:
      - Stadium
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Old Trafford"
            capacity: 74879
            location: "Manchester, UK"
    responses:
      201:
        description: Stadium created successfully
        examples:
          application/json: {
            "id": 1,
            "name": "Old Trafford",
            "capacity": 74879,
            "location": "Manchester, UK"
          }
    """
    content = request.get_json()
    stadium = Stadium.create_from_dto(content)
    stadium_controller.create(stadium)
    return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.CREATED)


@stadium_bp.route('/<int:stadium_id>', methods=['GET'])
def get_stadium(stadium_id: int) -> Response:
    """
    Get stadium by ID
    ---
    tags:
      - Stadium
    parameters:
      - name: stadium_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Single stadium
        examples:
          application/json: {
            "id": 1,
            "name": "Old Trafford",
            "capacity": 74879,
            "location": "Manchester, UK"
          }
      404:
        description: Stadium not found
    """
    return make_response(jsonify(stadium_controller.find_by_id(stadium_id)), HTTPStatus.OK)


@stadium_bp.route('/<int:stadium_id>', methods=['PUT'])
def update_stadium(stadium_id: int) -> Response:
    """
    Update a stadium (full update)
    ---
    tags:
      - Stadium
    parameters:
      - name: stadium_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    requestBody:
      required: true
      content:
        application/json:
          example:
            id: 1
            name: "Old Trafford"
            capacity: 74879
            location: "Manchester, UK"
    responses:
      200:
        description: Stadium updated successfully
        examples:
          application/json: "Stadium updated"
      404:
        description: Stadium not found
    """
    content = request.get_json()
    stadium = Stadium.create_from_dto(content)
    stadium_controller.update(stadium_id, stadium)
    return make_response("Stadium updated", HTTPStatus.OK)


@stadium_bp.route('/<int:stadium_id>', methods=['PATCH'])
def patch_stadium(stadium_id: int) -> Response:
    """
    Partially update a stadium
    ---
    tags:
      - Stadium
    parameters:
      - name: stadium_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "New Stadium Name"
    responses:
      200:
        description: Stadium partially updated
        examples:
          application/json: "Stadium updated"
      404:
        description: Stadium not found
    """
    content = request.get_json()
    stadium_controller.patch(stadium_id, content)
    return make_response("Stadium updated", HTTPStatus.OK)


@stadium_bp.route('/<int:stadium_id>', methods=['DELETE'])
def delete_stadium(stadium_id: int) -> Response:
    """
    Delete a stadium by ID
    ---
    tags:
      - Stadium
    parameters:
      - name: stadium_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Stadium deleted
        examples:
          application/json: "Stadium deleted"
      404:
        description: Stadium not found
    """
    stadium_controller.delete(stadium_id)
    return make_response("Stadium deleted", HTTPStatus.OK)
