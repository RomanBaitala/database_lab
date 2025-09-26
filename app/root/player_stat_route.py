from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from ..controller import player_stat_controller
from ..domain.player_stat import PlayerStat

player_stat_bp = Blueprint('player_stat', __name__, url_prefix='/player_stat')


@player_stat_bp.route('', methods=['GET'])
@jwt_required()
def get_all_player_stats() -> Response:
    """
    Get all player stats
    ---
    tags:
      - PlayerStat
    responses:
      200:
        description: List of all player stats
        examples:
          application/json: [
            {
              "id": 1,
              "player_id": 1,
              "games_played": 30,
              "scored": 15,
              "games_mark": 8.5
            }
          ]
    """
    return make_response(jsonify(player_stat_controller.find_all()), HTTPStatus.OK)


@player_stat_bp.route('', methods=['POST'])
@jwt_required()
def create_player_stat() -> Response:
    """
    Create a new player stat
    ---
    tags:
      - PlayerStat
    requestBody:
      required: true
      content:
        application/json:
          example:
            player_id: 1
            games_played: 30
            scored: 15
            games_mark: 8.5
    responses:
      201:
        description: Player stat created successfully
        examples:
          application/json: {
            "id": 1,
            "player_id": 1,
            "games_played": 30,
            "scored": 15,
            "games_mark": 8.5
          }
    """
    content = request.get_json()
    player_stat = PlayerStat.create_from_dto(content)
    player_stat_controller.create(player_stat)
    return make_response(jsonify(player_stat.put_into_dto()), HTTPStatus.CREATED)


@player_stat_bp.route('/<int:player_stat_id>', methods=['GET'])
@jwt_required()
def get_player_stat(player_stat_id: int) -> Response:
    """
    Get player stat by ID
    ---
    tags:
      - PlayerStat
    parameters:
      - name: player_stat_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Single player stat
        examples:
          application/json: {
            "id": 1,
            "player_id": 1,
            "games_played": 30,
            "scored": 15,
            "games_mark": 8.5
          }
      404:
        description: Player stat not found
    """
    return make_response(jsonify(player_stat_controller.find_by_id(player_stat_id)), HTTPStatus.OK)


@player_stat_bp.route('/<int:player_stat_id>', methods=['PUT'])
@jwt_required()
def update_player_stat(player_stat_id: int) -> Response:
    """
    Update a player stat (full update)
    ---
    tags:
      - PlayerStat
    parameters:
      - name: player_stat_id
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
            player_id: 1
            games_played: 30
            scored: 15
            games_mark: 8.5
    responses:
      200:
        description: Player stat updated successfully
        examples:
          application/json: "PlayerStat updated"
      404:
        description: Player stat not found
    """
    content = request.get_json()
    player_stat = PlayerStat.create_from_dto(content)
    player_stat_controller.update(player_stat_id, player_stat)
    return make_response("PlayerStat updated", HTTPStatus.OK)


@player_stat_bp.route('/<int:player_stat_id>', methods=['PATCH'])
@jwt_required()
def patch_player_stat(player_stat_id: int) -> Response:
    """
    Partially update a player stat
    ---
    tags:
      - PlayerStat
    parameters:
      - name: player_stat_id
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
            games_mark: 9.0
            scored: 16
    responses:
      200:
        description: Player stat partially updated
        examples:
          application/json: "PlayerStat updated"
      404:
        description: Player stat not found
    """
    content = request.get_json()
    player_stat_controller.patch(player_stat_id, content)
    return make_response("PlayerStat updated", HTTPStatus.OK)


@player_stat_bp.route('/<int:player_stat_id>', methods=['DELETE'])
@jwt_required()
def delete_player_stat(player_stat_id: int) -> Response:
    """
    Delete a player stat by ID
    ---
    tags:
      - PlayerStat
    parameters:
      - name: player_stat_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Player stat deleted
        examples:
          application/json: "PlayerStat deleted"
      404:
        description: Player stat not found
    """
    player_stat_controller.delete(player_stat_id)
    return make_response("PlayerStat deleted", HTTPStatus.OK)
