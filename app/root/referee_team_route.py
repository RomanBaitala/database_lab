from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from ..controller import referee_team_controller
from ..domain.referee_team import RefereeTeam

referee_team_bp = Blueprint('referee_team', __name__, url_prefix='/referee_team')


@referee_team_bp.route('', methods=['GET'])
@jwt_required()
def get_all_referee_teams() -> Response:
    """
    Get all referee teams
    ---
    tags:
      - RefereeTeam
    responses:
      200:
        description: List of all referee teams
        examples:
          application/json: [
            {
              "id": 1,
              "name": "Premier Referees",
              "league_id": 1
            }
          ]
    """
    return make_response(jsonify(referee_team_controller.find_all()), HTTPStatus.OK)


@referee_team_bp.route('', methods=['POST'])
@jwt_required()
def create_referee_team() -> Response:
    """
    Create a new referee team
    ---
    tags:
      - RefereeTeam
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Premier Referees"
            league_id: 1
    responses:
      201:
        description: Referee team created successfully
        examples:
          application/json: {
            "id": 1,
            "name": "Premier Referees",
            "league_id": 1
          }
    """
    content = request.get_json()
    referee_team = RefereeTeam.create_from_dto(content)
    referee_team_controller.create(referee_team)
    return make_response(jsonify(referee_team.put_into_dto()), HTTPStatus.CREATED)


@referee_team_bp.route('/<int:referee_team_id>', methods=['GET'])
@jwt_required()
def get_referee_team(referee_team_id: int) -> Response:
    """
    Get referee team by ID
    ---
    tags:
      - RefereeTeam
    parameters:
      - name: referee_team_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Single referee team
        examples:
          application/json: {
            "id": 1,
            "name": "Premier Referees",
            "league_id": 1
          }
      404:
        description: Referee team not found
    """
    return make_response(jsonify(referee_team_controller.find_by_id(referee_team_id)), HTTPStatus.OK)


@referee_team_bp.route('/<int:referee_team_id>', methods=['PUT'])
@jwt_required()
def update_referee_team(referee_team_id: int) -> Response:
    """
    Update a referee team (full update)
    ---
    tags:
      - RefereeTeam
    parameters:
      - name: referee_team_id
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
            name: "Premier Referees"
            league_id: 1
    responses:
      200:
        description: Referee team updated successfully
        examples:
          application/json: "RefereeTeam updated"
      404:
        description: Referee team not found
    """
    content = request.get_json()
    referee_team = RefereeTeam.create_from_dto(content)
    referee_team_controller.update(referee_team_id, referee_team)
    return make_response("RefereeTeam updated", HTTPStatus.OK)


@referee_team_bp.route('/<int:referee_team_id>', methods=['PATCH'])
@jwt_required()
def patch_referee_team(referee_team_id: int) -> Response:
    """
    Partially update a referee team
    ---
    tags:
      - RefereeTeam
    parameters:
      - name: referee_team_id
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
            name: "Updated Referee Team"
    responses:
      200:
        description: Referee team partially updated
        examples:
          application/json: "RefereeTeam updated"
      404:
        description: Referee team not found
    """
    content = request.get_json()
    referee_team_controller.patch(referee_team_id, content)
    return make_response("RefereeTeam updated", HTTPStatus.OK)


@referee_team_bp.route('/<int:referee_team_id>', methods=['DELETE'])
@jwt_required()
def delete_referee_team(referee_team_id: int) -> Response:
    """
    Delete a referee team by ID
    ---
    tags:
      - RefereeTeam
    parameters:
      - name: referee_team_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Referee team deleted
        examples:
          application/json: "RefereeTeam deleted"
      404:
        description: Referee team not found
    """
    referee_team_controller.delete(referee_team_id)
    return make_response("RefereeTeam deleted", HTTPStatus.OK)
