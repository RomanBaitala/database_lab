from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import player_controller
from ..domain.player import Player

player_bp = Blueprint('player', __name__, url_prefix='/player')


@player_bp.route('', methods=['GET'])
def get_all_players() -> Response:
    """
    Get all players
    ---
    tags:
      - Player
    responses:
      200:
        description: List of all players
        examples:
          application/json: [
            {
              "id": 1,
              "name": "Cristiano",
              "surname": "Ronaldo",
              "age": 38,
              "nationality": "Portugal",
              "team_id": 5
            }
          ]
    """
    return make_response(jsonify(player_controller.find_all()), HTTPStatus.OK)


@player_bp.route('', methods=['POST'])
def create_player() -> Response:
    """
    Create a new player
    ---
    tags:
      - Player
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Cristiano"
            surname: "Ronaldo"
            age: 38
            nationality: "Portugal"
            team_id: 5
    responses:
      201:
        description: Player created successfully
        examples:
          application/json: {
            "id": 1,
            "name": "Cristiano",
            "surname": "Ronaldo",
            "age": 38,
            "nationality": "Portugal",
            "team_id": 5
          }
    """
    content = request.get_json()
    player = Player.create_from_dto(content)
    player_controller.create(player)
    return make_response(jsonify(player.put_into_dto()), HTTPStatus.CREATED)


@player_bp.route('/<int:player_id>', methods=['GET'])
def get_player(player_id: int) -> Response:
    """
    Get player by ID
    ---
    tags:
      - Player
    parameters:
      - name: player_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Single player
        examples:
          application/json: {
            "id": 1,
            "name": "Cristiano",
            "surname": "Ronaldo",
            "age": 38,
            "nationality": "Portugal",
            "team_id": 5
          }
      404:
        description: Player not found
    """
    return make_response(jsonify(player_controller.find_by_id(player_id)), HTTPStatus.OK)


@player_bp.route('/<int:player_id>', methods=['PUT'])
def update_player(player_id: int) -> Response:
    """
    Update a player (full update)
    ---
    tags:
      - Player
    parameters:
      - name: player_id
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
            name: "Cristiano"
            surname: "Ronaldo"
            age: 38
            nationality: "Portugal"
            team_id: 5
    responses:
      200:
        description: Player updated successfully
        examples:
          application/json: "Player updated"
      404:
        description: Player not found
    """
    content = request.get_json()
    player = Player.create_from_dto(content)
    player_controller.update(player_id, player)
    return make_response("Player updated", HTTPStatus.OK)


@player_bp.route('/<int:player_id>', methods=['PATCH'])
def patch_player(player_id: int) -> Response:
    """
    Partially update a player
    ---
    tags:
      - Player
    parameters:
      - name: player_id
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
            age: 39
            team_id: 6
    responses:
      200:
        description: Player partially updated
        examples:
          application/json: "Player updated"
      404:
        description: Player not found
    """
    content = request.get_json()
    player_controller.patch(player_id, content)
    return make_response("Player updated", HTTPStatus.OK)


@player_bp.route('/<int:player_id>', methods=['DELETE'])
def delete_player(player_id: int) -> Response:
    """
    Delete a player by ID
    ---
    tags:
      - Player
    parameters:
      - name: player_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Player deleted
        examples:
          application/json: "Player deleted"
      404:
        description: Player not found
    """
    player_controller.delete(player_id)
    return make_response("Player deleted", HTTPStatus.OK)
