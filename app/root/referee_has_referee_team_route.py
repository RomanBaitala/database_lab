from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import referee_has_referee_team_controller
from ..domain.referee_has_referee_team import RefereeHasRefereeTeam

referee_has_referee_team_bp = Blueprint('referee_has_referee_team', __name__, url_prefix='/referee_has_referee_team')


@referee_has_referee_team_bp.route('', methods=['GET'])
def get_all_referee_has_referee_teams() -> Response:
    return make_response(jsonify(referee_has_referee_team_controller.find_all()), HTTPStatus.OK)


@referee_has_referee_team_bp.route('', methods=['POST'])
def create_referee_has_referee_team() -> Response:
    content = request.get_json()
    referee_has_referee_team = RefereeHasRefereeTeam.create_from_dto(content)
    referee_has_referee_team_controller.create(referee_has_referee_team)
    return make_response(jsonify(referee_has_referee_team.put_into_dto()), HTTPStatus.CREATED)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['GET'])
def get_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    return make_response(jsonify(referee_has_referee_team_controller.find_by_id(referee_has_referee_team_id)), HTTPStatus.OK)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['PUT'])
def update_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    content = request.get_json()
    referee_has_referee_team = RefereeHasRefereeTeam.create_from_dto(content)
    referee_has_referee_team_controller.update(referee_has_referee_team_id, referee_has_referee_team)
    return make_response("RefereeHasRefereeTeam updated", HTTPStatus.OK)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['PATCH'])
def patch_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    content = request.get_json()
    referee_has_referee_team_controller.patch(referee_has_referee_team_id, content)
    return make_response("RefereeHasRefereeTeam updated", HTTPStatus.OK)


@referee_has_referee_team_bp.route('/<int:referee_has_referee_team_id>', methods=['DELETE'])
def delete_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    referee_has_referee_team_controller.delete(referee_has_referee_team_id)
    return make_response("RefereeHasRefereeTeam deleted", HTTPStatus.OK)
