from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import referee_team_controller
from ..domain.referee_team import RefereeTeam

referee_team_bp = Blueprint('referee_team', __name__, url_prefix='/referee_team')


@referee_team_bp.route('', methods=['GET'])
def get_all_referee_teams() -> Response:
    return make_response(jsonify(referee_team_controller.find_all()), HTTPStatus.OK)


@referee_team_bp.route('', methods=['POST'])
def create_referee_team() -> Response:
    content = request.get_json()
    referee_team = RefereeTeam.create_from_dto(content)
    referee_team_controller.create(referee_team)
    return make_response(jsonify(referee_team.put_into_dto()), HTTPStatus.CREATED)


@referee_team_bp.route('/<int:referee_team_id>', methods=['GET'])
def get_referee_team(referee_team_id: int) -> Response:
    return make_response(jsonify(referee_team_controller.find_by_id(referee_team_id)), HTTPStatus.OK)


@referee_team_bp.route('/<int:referee_team_id>', methods=['PUT'])
def update_referee_team(referee_team_id: int) -> Response:
    content = request.get_json()
    referee_team = RefereeTeam.create_from_dto(content)
    referee_team_controller.update(referee_team_id, referee_team)
    return make_response("RefereeTeam updated", HTTPStatus.OK)


@referee_team_bp.route('/<int:referee_team_id>', methods=['PATCH'])
def patch_referee_team(referee_team_id: int) -> Response:
    content = request.get_json()
    referee_team_controller.patch(referee_team_id, content)
    return make_response("RefereeTeam updated", HTTPStatus.OK)


@referee_team_bp.route('/<int:referee_team_id>', methods=['DELETE'])
def delete_referee_team(referee_team_id: int) -> Response:
    referee_team_controller.delete(referee_team_id)
    return make_response("RefereeTeam deleted", HTTPStatus.OK)
