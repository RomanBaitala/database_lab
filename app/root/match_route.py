from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import match_controller
from ..domain.match import FMatch

match_bp = Blueprint('match', __name__, url_prefix='/match')


@match_bp.route('', methods=['GET'])
def get_all_matches():
    """
    Get all matches
    ---
    tags:
      - Match
    responses:
      200:
        description: List of matches
        examples:
          application/json: [
            {
              "id": 1,
              "home_team_id": 1,
              "away_team_id": 2,
              "home_start_lineup": 1,
              "away_start_lineup": 2,
              "referee_team_id": 1,
              "stadium_id": 1,
              "team_league_id": 1
            }
          ]
    """
    return make_response(jsonify(match_controller.find_all()), HTTPStatus.OK)


@match_bp.route('', methods=['POST'])
def create_match():
    """
    Create a new match
    ---
    tags:
      - Match
    consumes:
      - application/json
    parameters:
      - in: body
        name: match
        required: true
        schema:
          type: object
          properties:
            home_team_id:
              type: integer
            away_team_id:
              type: integer
            home_start_lineup:
              type: integer
            away_start_lineup:
              type: integer
            referee_team_id:
              type: integer
            stadium_id:
              type: integer
            team_league_id:
              type: integer
          required:
            - home_team_id
            - away_team_id
            - home_start_lineup
            - away_start_lineup
            - referee_team_id
            - stadium_id
            - team_league_id
          example:
            home_team_id: 1
            away_team_id: 2
            home_start_lineup: 1
            away_start_lineup: 2
            referee_team_id: 1
            stadium_id: 1
            team_league_id: 1
    responses:
      201:
        description: Match created
        examples:
          application/json: {
            "id": 1,
            "home_team_id": 1,
            "away_team_id": 2,
            "home_start_lineup": 1,
            "away_start_lineup": 2,
            "referee_team_id": 1,
            "stadium_id": 1,
            "team_league_id": 1
          }
    """
    content = request.get_json()
    match = FMatch.create_from_dto(content)
    match_controller.create(match)
    return make_response(jsonify(match.put_into_dto()), HTTPStatus.CREATED)


@match_bp.route('/<int:match_id>', methods=['GET'])
def get_match(match_id: int):
    """
    Get a match by ID
    ---
    tags:
      - Match
    parameters:
      - in: path
        name: match_id
        type: integer
        required: true
        description: ID of the match
    responses:
      200:
        description: Match found
        examples:
          application/json: {
            "id": 1,
            "home_team_id": 1,
            "away_team_id": 2,
            "home_start_lineup": 1,
            "away_start_lineup": 2,
            "referee_team_id": 1,
            "stadium_id": 1,
            "team_league_id": 1
          }
      404:
        description: Match not found
        examples:
          application/json: {"error": "Match not found"}
    """
    match = match_controller.find_by_id(match_id)
    if match is None:
        return make_response(jsonify({"error": "Match not found"}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify(match), HTTPStatus.OK)


@match_bp.route('/<int:match_id>', methods=['PUT'])
def update_match(match_id: int):
    """
    Update a match by ID
    ---
    tags:
      - Match
    consumes:
      - application/json
    parameters:
      - in: path
        name: match_id
        type: integer
        required: true
        description: ID of the match to update
      - in: body
        name: match
        required: true
        schema:
          type: object
          properties:
            home_team_id:
              type: integer
            away_team_id:
              type: integer
            home_start_lineup:
              type: integer
            away_start_lineup:
              type: integer
            referee_team_id:
              type: integer
            stadium_id:
              type: integer
            team_league_id:
              type: integer
          example:
            home_team_id: 1
            away_team_id: 2
            home_start_lineup: 1
            away_start_lineup: 2
            referee_team_id: 1
            stadium_id: 1
            team_league_id: 1
    responses:
      200:
        description: Match updated successfully
        examples:
          application/json: "Match updated"
      404:
        description: Match not found
        examples:
          application/json: {"error": "Match not found"}
    """
    content = request.get_json()
    updated = match_controller.update(match_id, FMatch.create_from_dto(content))
    if not updated:
        return make_response(jsonify({"error": "Match not found"}), HTTPStatus.NOT_FOUND)
    return make_response("Match updated", HTTPStatus.OK)


@match_bp.route('/<int:match_id>', methods=['PATCH'])
def patch_match(match_id: int):
    """
    Partially update a match by ID
    ---
    tags:
      - Match
    consumes:
      - application/json
    parameters:
      - in: path
        name: match_id
        type: integer
        required: true
        description: ID of the match to update
      - in: body
        name: match
        required: true
        schema:
          type: object
          properties:
            home_start_lineup:
              type: integer
            away_start_lineup:
              type: integer
          example:
            home_start_lineup: 2
    responses:
      200:
        description: Match updated successfully
        examples:
          application/json: "Match updated"
      404:
        description: Match not found
        examples:
          application/json: {"error": "Match not found"}
    """
    content = request.get_json()
    updated = match_controller.patch(match_id, content)
    if not updated:
        return make_response(jsonify({"error": "Match not found"}), HTTPStatus.NOT_FOUND)
    return make_response("Match updated", HTTPStatus.OK)


@match_bp.route('/<int:match_id>', methods=['DELETE'])
def delete_match(match_id: int):
    """
    Delete a match by ID
    ---
    tags:
      - Match
    parameters:
      - in: path
        name: match_id
        type: integer
        required: true
        description: ID of the match to delete
    responses:
      200:
        description: Match deleted successfully
        examples:
          application/json: "Match deleted"
      404:
        description: Match not found
        examples:
          application/json: {"error": "Match not found"}
    """
    deleted = match_controller.delete(match_id)
    if not deleted:
        return make_response(jsonify({"error": "Match not found"}), HTTPStatus.NOT_FOUND)
    return make_response("Match deleted", HTTPStatus.OK)

