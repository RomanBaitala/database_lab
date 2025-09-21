from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import referee_controller
from ..domain.referee import Referee

referee_bp = Blueprint('referee', __name__, url_prefix='/referee')


@referee_bp.route('', methods=['GET'])
def get_all_referees() -> Response:
    """
    Get all referees
    ---
    tags:
      - Referee
    responses:
      200:
        description: List of all referees
        examples:
          application/json: [
            {
              "id": 1,
              "name": "Michael",
              "surname": "Oliver",
              "age": 38,
              "gender": 1,
              "position": "Center Referee"
            }
          ]
    """
    return make_response(jsonify(referee_controller.find_all()), HTTPStatus.OK)


@referee_bp.route('', methods=['POST'])
def create_referee() -> Response:
    """
    Create a new referee
    ---
    tags:
      - Referee
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Michael"
            surname: "Oliver"
            age: 38
            gender: 1
            position: "Center Referee"
    responses:
      201:
        description: Referee created successfully
        examples:
          application/json: {
            "id": 1,
            "name": "Michael",
            "surname": "Oliver",
            "age": 38,
            "gender": 1,
            "position": "Center Referee"
          }
    """
    content = request.get_json()
    referee = Referee.create_from_dto(content)
    referee_controller.create(referee)
    return make_response(jsonify(referee.put_into_dto()), HTTPStatus.CREATED)


@referee_bp.route('/<int:referee_id>', methods=['GET'])
def get_referee(referee_id: int) -> Response:
    """
    Get referee by ID
    ---
    tags:
      - Referee
    parameters:
      - name: referee_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Single referee
        examples:
          application/json: {
            "id": 1,
            "name": "Michael",
            "surname": "Oliver",
            "age": 38,
            "gender": 1,
            "position": "Center Referee"
          }
      404:
        description: Referee not found
    """
    return make_response(jsonify(referee_controller.find_by_id(referee_id)), HTTPStatus.OK)


@referee_bp.route('/<int:referee_id>', methods=['PUT'])
def update_referee(referee_id: int) -> Response:
    """
    Update a referee (full update)
    ---
    tags:
      - Referee
    parameters:
      - name: referee_id
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
            name: "Michael"
            surname: "Oliver"
            age: 38
            gender: 1
            position: "Center Referee"
    responses:
      200:
        description: Referee updated successfully
        examples:
          application/json: "Referee updated"
      404:
        description: Referee not found
    """
    content = request.get_json()
    referee = Referee.create_from_dto(content)
    referee_controller.update(referee_id, referee)
    return make_response("Referee updated", HTTPStatus.OK)


@referee_bp.route('/<int:referee_id>', methods=['PATCH'])
def patch_referee(referee_id: int) -> Response:
    """
    Partially update a referee
    ---
    tags:
      - Referee
    parameters:
      - name: referee_id
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
            position: "Assistant Referee"
    responses:
      200:
        description: Referee partially updated
        examples:
          application/json: "Referee updated"
      404:
        description: Referee not found
    """
    content = request.get_json()
    referee_controller.patch(referee_id, content)
    return make_response("Referee updated", HTTPStatus.OK)


@referee_bp.route('/<int:referee_id>', methods=['DELETE'])
def delete_referee(referee_id: int) -> Response:
    """
    Delete a referee by ID
    ---
    tags:
      - Referee
    parameters:
      - name: referee_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Referee deleted
        examples:
          application/json: "Referee deleted"
      404:
        description: Referee not found
    """
    referee_controller.delete(referee_id)
    return make_response("Referee deleted", HTTPStatus.OK)

