from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import league_controller
from ..domain.league import League

league_bp = Blueprint('league', __name__, url_prefix='/league')


@league_bp.route('', methods=['GET'])
def get_all_leagues():
    """
    Get all leagues
    ---
    tags:
      - League
    responses:
      200:
        description: List of leagues
        examples:
          application/json: [{"id": 1, "name": "Premier League"}]
    """
    return make_response(jsonify(league_controller.find_all()), HTTPStatus.OK)


@league_bp.route('', methods=['POST'])
def create_league():
    """
    Create a new league
    ---
    tags:
      - League
    consumes:
      - application/json
    parameters:
      - in: body
        name: league
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
          required:
            - name
          example:
            name: "Premier League"
    responses:
      201:
        description: League created
        examples:
          application/json: {"id": 1, "name": "Premier League"}
    """
    content = request.get_json()
    league = League.create_from_dto(content)
    league_controller.create(league)
    return make_response(jsonify(league.put_into_dto()), HTTPStatus.CREATED)


@league_bp.route('/<int:league_id>', methods=['GET'])
def get_league(league_id: int):
    """
    Get a league by ID
    ---
    tags:
      - League
    parameters:
      - in: path
        name: league_id
        type: integer
        required: true
        description: ID of the league
    responses:
      200:
        description: League found
        examples:
          application/json: {
            "id": 1,
            "name": "Premier League",
            "team_count": 20
          }
      404:
        description: League not found
        examples:
          application/json: {"error": "League not found"}
    """
    league = league_controller.find_by_id(league_id)
    if league is None:
        return make_response(jsonify({"error": "League not found"}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify(league), HTTPStatus.OK)


@league_bp.route('/<int:league_id>', methods=['PUT'])
def update_league(league_id: int):
    """
    Update a league by ID
    ---
    tags:
      - League
    consumes:
      - application/json
    parameters:
      - in: path
        name: league_id
        type: integer
        required: true
        description: ID of the league to update
      - in: body
        name: league
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
          required:
            - name
          example:
            name: "Premier League"
    responses:
      200:
        description: League updated successfully
        examples:
          application/json: "League updated"
      404:
        description: League not found
        examples:
          application/json: {"error": "League not found"}
    """
    content = request.get_json()
    updated = league_controller.update(league_id, League.create_from_dto(content))
    if not updated:
        return make_response(jsonify({"error": "League not found"}), HTTPStatus.NOT_FOUND)
    return make_response("League updated", HTTPStatus.OK)


@league_bp.route('/<int:league_id>', methods=['PATCH'])
def patch_league(league_id: int):
    """
    Partially update a league by ID
    ---
    tags:
      - League
    consumes:
      - application/json
    parameters:
      - in: path
        name: league_id
        type: integer
        required: true
        description: ID of the league to update
      - in: body
        name: league
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
          example:
            name: "Championship League"
    responses:
      200:
        description: League updated successfully
        examples:
          application/json: "League updated"
      404:
        description: League not found
        examples:
          application/json: {"error": "League not found"}
    """
    content = request.get_json()
    updated = league_controller.patch(league_id, content)
    if not updated:
        return make_response(jsonify({"error": "League not found"}), HTTPStatus.NOT_FOUND)
    return make_response("League updated", HTTPStatus.OK)


@league_bp.route('/<int:league_id>', methods=['DELETE'])
def delete_league(league_id: int):
    """
    Delete a league by ID
    ---
    tags:
      - League
    parameters:
      - in: path
        name: league_id
        type: integer
        required: true
        description: ID of the league to delete
    responses:
      200:
        description: League deleted successfully
        examples:
          application/json: "League deleted"
      404:
        description: League not found
        examples:
          application/json: {"error": "League not found"}
    """
    deleted = league_controller.delete(league_id)
    if not deleted:
        return make_response(jsonify({"error": "League not found"}), HTTPStatus.NOT_FOUND)
    return make_response("League deleted", HTTPStatus.OK)

