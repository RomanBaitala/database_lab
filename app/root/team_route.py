from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from ..controller import team_controller
from ..domain.team import Team

team_bp = Blueprint('team', __name__, url_prefix='/team')


@team_bp.route('', methods=['GET'])
@jwt_required()
def get_all_teams() -> Response:
    """
    Get all teams
    ---
    tags:
      - Team
    responses:
      200:
        description: List of all teams
        content:
          application/json:
            example: [
              {
                "id": 1,
                "name": "Manchester United",
                "coach": "Erik ten Hag",
                "league_id": 1,
                "stadium_id": 1,
                "players": [],
                "matches": []
              }
            ]
    """
    return make_response(jsonify(team_controller.find_all()), HTTPStatus.OK)


@team_bp.route('', methods=['POST'])
@jwt_required()
def create_team() -> Response:
    """
    Create a new team
    ---
    tags:
      - Team
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Manchester United"
            coach: "Erik ten Hag"
            league_id: 1
            stadium_id: 1
            players: []
            matches: []
    responses:
      201:
        description: Team created successfully
        content:
          application/json:
            example:
              id: 1
              name: "Manchester United"
              coach: "Erik ten Hag"
              league_id: 1
              stadium_id: 1
              players: []
              matches: []
    """
    content = request.get_json()
    team = Team.create_from_dto(content)
    team_controller.create(team)
    return make_response(jsonify(team.put_into_dto()), HTTPStatus.CREATED)


@team_bp.route('/<int:team_id>', methods=['GET'])
@jwt_required()
def get_team(team_id: int) -> Response:
    """
    Get a team by ID
    ---
    tags:
      - Team
    parameters:
      - name: team_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Team details
        content:
          application/json:
            example:
              id: 1
              name: "Manchester United"
              coach: "Erik ten Hag"
              league_id: 1
              stadium_id: 1
              players: []
              matches: []
      404:
        description: Team not found
    """
    return make_response(jsonify(team_controller.find_by_id(team_id)), HTTPStatus.OK)


@team_bp.route('/<int:team_id>', methods=['PUT'])
@jwt_required()
def update_team(team_id: int) -> Response:
    """
    Update a team (full update)
    ---
    tags:
      - Team
    parameters:
      - name: team_id
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
            name: "Manchester United"
            coach: "Erik ten Hag"
            league_id: 1
            stadium_id: 1
            players: []
            matches: []
    responses:
      200:
        description: Team updated successfully
        content:
          application/json:
            example: "Team updated"
      404:
        description: Team not found
    """
    content = request.get_json()
    team = Team.create_from_dto(content)
    team_controller.update(team_id, team)
    return make_response("Team updated", HTTPStatus.OK)


@team_bp.route('/<int:team_id>', methods=['PATCH'])
@jwt_required()
def patch_team(team_id: int) -> Response:
    """
    Partially update a team
    ---
    tags:
      - Team
    parameters:
      - name: team_id
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
            coach: "Erik ten Hag"
    responses:
      200:
        description: Team partially updated
        content:
          application/json:
            example: "Team updated"
      404:
        description: Team not found
    """
    content = request.get_json()
    team_controller.patch(team_id, content)
    return make_response("Team updated", HTTPStatus.OK)


@team_bp.route('/<int:team_id>', methods=['DELETE'])
@jwt_required()
def delete_team(team_id: int) -> Response:
    """
    Delete a team by ID
    ---
    tags:
      - Team
    parameters:
      - name: team_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Team deleted
        content:
          application/json:
            example: "Team deleted"
      404:
        description: Team not found
    """
    team_controller.delete(team_id)
    return make_response("Team deleted", HTTPStatus.OK)
