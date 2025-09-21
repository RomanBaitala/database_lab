from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import referee_has_referee_team_controller
from ..domain.referee_has_referee_team import RefereeHasRefereeTeam

referee_has_referee_team_bp = Blueprint('referee_has_referee_team', __name__, url_prefix='/referee_has_referee_team')


@referee_has_referee_team_bp.route('', methods=['GET'])
def get_all_referee_has_referee_teams() -> Response:
    """
    Get all referee_has_referee_teams
    ---
    tags:
      - RefereeHasRefereeTeam
    responses:
      200:
        description: List of all referee_has_referee_teams
        examples:
          application/json: [
            {
              "id": 1,
              "referee_id": 1,
              "referee_team_id": 1
            }
          ]
    """
    return make_response(jsonify(referee_has_referee_team_controller.find_all()), HTTPStatus.OK)


@referee_has_referee_team_bp.route('', methods=['POST'])
def create_referee_has_referee_team() -> Response:
    """
    Create a new referee_has_referee_team
    ---
    tags:
      - RefereeHasRefereeTeam
    requestBody:
      required: true
      content:
        application/json:
          example:
            referee_id: 1
            referee_team_id: 1
    responses:
      201:
        description: RefereeHasRefereeTeam created successfully
        examples:
          application/json: {
            "id": 1,
            "referee_id": 1,
            "referee_team_id": 1
          }
    """
    content = request.get_json()
    referee_has_referee_team = RefereeHasRefereeTeam.create_from_dto(content)
    referee_has_referee_team_controller.create(referee_has_referee_team)
    return make_response(jsonify(referee_has_referee_team.put_into_dto()), HTTPStatus.CREATED)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['GET'])
def get_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    """
    Get referee_has_referee_team by ID
    ---
    tags:
      - RefereeHasRefereeTeam
    parameters:
      - name: referee_has_referee_team_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Single referee_has_referee_team
        examples:
          application/json: {
            "id": 1,
            "referee_id": 1,
            "referee_team_id": 1
          }
      404:
        description: RefereeHasRefereeTeam not found
    """
    return make_response(jsonify(referee_has_referee_team_controller.find_by_id(referee_has_referee_team_id)), HTTPStatus.OK)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['PUT'])
def update_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    """
    Update a referee_has_referee_team (full update)
    ---
    tags:
      - RefereeHasRefereeTeam
    parameters:
      - name: referee_has_referee_team_id
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
            referee_id: 1
            referee_team_id: 1
    responses:
      200:
        description: RefereeHasRefereeTeam updated successfully
        examples:
          application/json: "RefereeHasRefereeTeam updated"
      404:
        description: RefereeHasRefereeTeam not found
    """
    content = request.get_json()
    referee_has_referee_team = RefereeHasRefereeTeam.create_from_dto(content)
    referee_has_referee_team_controller.update(referee_has_referee_team_id, referee_has_referee_team)
    return make_response("RefereeHasRefereeTeam updated", HTTPStatus.OK)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['PATCH'])
def patch_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    """
    Partially update a referee_has_referee_team
    ---
    tags:
      - RefereeHasRefereeTeam
    parameters:
      - name: referee_has_referee_team_id
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
            referee_team_id: 2
    responses:
      200:
        description: RefereeHasRefereeTeam partially updated
        examples:
          application/json: "RefereeHasRefereeTeam updated"
      404:
        description: RefereeHasRefereeTeam not found
    """
    content = request.get_json()
    referee_has_referee_team_controller.patch(referee_has_referee_team_id, content)
    return make_response("RefereeHasRefereeTeam updated", HTTPStatus.OK)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['DELETE'])
def delete_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    """
    Delete a referee_has_referee_team by ID
    ---
    tags:
      - RefereeHasRefereeTeam
    parameters:
      - name: referee_has_referee_team_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: RefereeHasRefereeTeam deleted
        examples:
          application/json: "RefereeHasRefereeTeam deleted"
      404:
        description: RefereeHasRefereeTeam not found
    """
    referee_has_referee_team_controller.delete(referee_has_referee_team_id)
    return make_response("RefereeHasRefereeTeam deleted", HTTPStatus.OK)
