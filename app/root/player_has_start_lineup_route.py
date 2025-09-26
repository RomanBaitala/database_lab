from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from ..controller import player_has_start_lineup_controller
from ..domain.player_has_start_lineup import PlayerHasStartLineup

player_has_start_lineup_bp = Blueprint('player_has_start_lineup', __name__, url_prefix='/player_has_start_lineup')


@player_has_start_lineup_bp.route('', methods=['GET'])
@jwt_required()
def get_all_player_has_start_lineups() -> Response:
    """
    Get all player-start_lineup relations
    ---
    tags:
      - PlayerHasStartLineup
    responses:
      200:
        description: A list of player-start_lineup relations
        examples:
          application/json: [
            {
              "id": 1,
              "player_id": 1,
              "start_lineup_id": 1
            }
          ]
    """
    return make_response(jsonify(player_has_start_lineup_controller.find_all()), HTTPStatus.OK)


@player_has_start_lineup_bp.route('', methods=['POST'])
@jwt_required()
def create_player_has_start_lineup() -> Response:
    """
    Create a new player-start_lineup relation
    ---
    tags:
      - PlayerHasStartLineup
    requestBody:
      required: true
      content:
        application/json:
          example:
            player_id: 1
            start_lineup_id: 1
    responses:
      201:
        description: Player-start_lineup relation created
        examples:
          application/json: {
            "id": 1,
            "player_id": 1,
            "start_lineup_id": 1
          }
    """
    content = request.get_json()
    player_has_start_lineup = PlayerHasStartLineup.create_from_dto(content)
    player_has_start_lineup_controller.create(player_has_start_lineup)
    return make_response(jsonify(player_has_start_lineup.put_into_dto()), HTTPStatus.CREATED)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['GET'])
@jwt_required()
def get_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    """
    Get player-start_lineup relation by ID
    ---
    tags:
      - PlayerHasStartLineup
    parameters:
      - name: player_has_start_lineup_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: A single player-start_lineup relation
        examples:
          application/json: {
            "id": 1,
            "player_id": 1,
            "start_lineup_id": 1
          }
      404:
        description: Not found
    """
    return make_response(jsonify(player_has_start_lineup_controller.find_by_id(player_has_start_lineup_id)), HTTPStatus.OK)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['PUT'])
@jwt_required()
def update_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    """
    Update a player-start_lineup relation (full update)
    ---
    tags:
      - PlayerHasStartLineup
    parameters:
      - name: player_has_start_lineup_id
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
            player_id: 1
            start_lineup_id: 1
    responses:
      200:
        description: Player-start_lineup updated successfully
        examples:
          application/json: "PlayerHasStartLineup updated"
      404:
        description: Not found
    """
    content = request.get_json()
    player_has_start_lineup = PlayerHasStartLineup.create_from_dto(content)
    player_has_start_lineup_controller.update(player_has_start_lineup_id, player_has_start_lineup)
    return make_response("PlayerHasStartLineup updated", HTTPStatus.OK)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['PATCH'])
@jwt_required()
def patch_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    """
    Partially update a player-start_lineup relation
    ---
    tags:
      - PlayerHasStartLineup
    parameters:
      - name: player_has_start_lineup_id
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
            start_lineup_id: 2
    responses:
      200:
        description: Player-start_lineup partially updated
        examples:
          application/json: "PlayerHasStartLineup updated"
      404:
        description: Not found
    """
    content = request.get_json()
    player_has_start_lineup_controller.patch(player_has_start_lineup_id, content)
    return make_response("PlayerHasStartLineup updated", HTTPStatus.OK)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['DELETE'])
@jwt_required()
def delete_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    """
    Delete a player-start_lineup relation by ID
    ---
    tags:
      - PlayerHasStartLineup
    parameters:
      - name: player_has_start_lineup_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Player-start_lineup deleted
        examples:
          application/json: "PlayerHasStartLineup deleted"
      404:
        description: Not found
    """
    player_has_start_lineup_controller.delete(player_has_start_lineup_id)
    return make_response("PlayerHasStartLineup deleted", HTTPStatus.OK)
