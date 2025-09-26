from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from ..controller import start_lineup_controller
from ..domain.start_lineup import StartLineup

start_lineup_bp = Blueprint('start_lineup', __name__, url_prefix='/start_lineup')


@start_lineup_bp.route('', methods=['GET'])
@jwt_required()
def get_all_start_lineups() -> Response:
    """
    Get all start lineups
    ---
    tags:
      - StartLineup
    responses:
      200:
        description: List of all start lineups
        examples:
          application/json: [
            {
              "id": 1,
              "start_players": [],
              "team_id": 1
            }
          ]
    """
    return make_response(jsonify(start_lineup_controller.find_all()), HTTPStatus.OK)


@start_lineup_bp.route('', methods=['POST'])
@jwt_required()
def create_start_lineup() -> Response:
    """
    Create a new start lineup
    ---
    tags:
      - StartLineup
    requestBody:
      required: true
      content:
        application/json:
          example:
            start_players: []
            team_id: 1
    responses:
      201:
        description: Start lineup created successfully
        examples:
          application/json: {
            "id": 1,
            "start_players": [],
            "team_id": 1
          }
    """
    content = request.get_json()
    start_lineup = StartLineup.create_from_dto(content)
    start_lineup_controller.create(start_lineup)
    return make_response(jsonify(start_lineup.put_into_dto()), HTTPStatus.CREATED)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['GET'])
@jwt_required()
def get_start_lineup(start_lineup_id: int) -> Response:
    """
    Get a start lineup by ID
    ---
    tags:
      - StartLineup
    parameters:
      - name: start_lineup_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Start lineup details
        examples:
          application/json: {
            "id": 1,
            "start_players": [],
            "team_id": 1
          }
      404:
        description: Start lineup not found
    """
    return make_response(jsonify(start_lineup_controller.find_by_id(start_lineup_id)), HTTPStatus.OK)



@start_lineup_bp.route('/<int:start_lineup_id>', methods=['PUT'])
@jwt_required()
def update_start_lineup(start_lineup_id: int) -> Response:
    """
    Update a start lineup (full update)
    ---
    tags:
      - StartLineup
    parameters:
      - name: start_lineup_id
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
            start_players: []
            team_id: 1
    responses:
      200:
        description: Start lineup updated successfully
        examples:
          application/json: "StartLineup updated"
      404:
        description: Start lineup not found
    """
    content = request.get_json()
    start_lineup = StartLineup.create_from_dto(content)
    start_lineup_controller.update(start_lineup_id, start_lineup)
    return make_response("StartLineup updated", HTTPStatus.OK)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['PATCH'])
@jwt_required()
def patch_start_lineup(start_lineup_id: int) -> Response:
    """
    Partially update a start lineup
    ---
    tags:
      - StartLineup
    parameters:
      - name: start_lineup_id
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
            start_players: []
    responses:
      200:
        description: Start lineup partially updated
        examples:
          application/json: "StartLineup updated"
      404:
        description: Start lineup not found
    """
    content = request.get_json()
    start_lineup_controller.patch(start_lineup_id, content)
    return make_response("StartLineup updated", HTTPStatus.OK)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['DELETE'])
@jwt_required()
def delete_start_lineup(start_lineup_id: int) -> Response:
    """
    Delete a start lineup by ID
    ---
    tags:
      - StartLineup
    parameters:
      - name: start_lineup_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Start lineup deleted
        examples:
          application/json: "StartLineup deleted"
      404:
        description: Start lineup not found
    """
    start_lineup_controller.delete(start_lineup_id)
    return make_response("StartLineup deleted", HTTPStatus.OK)
