from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import team_controller
from ..domain.team import Team

team_bp = Blueprint('team', __name__, url_prefix='/team')


@team_bp.route('', methods=['GET'])
def get_all_teams() -> Response:
    return make_response(jsonify(team_controller.find_all()), HTTPStatus.OK)


@team_bp.route('', methods=['POST'])
def create_team() -> Response:
    content = request.get_json()
    team = Team.create_from_dto(content)
    team_controller.create(team)
    return make_response(jsonify(team.put_into_dto()), HTTPStatus.CREATED)


@team_bp.route('/<int:team_id>', methods=['GET'])
def get_team(team_id: int) -> Response:
    return make_response(jsonify(team_controller.find_by_id(team_id)), HTTPStatus.OK)


@team_bp.route('/<int:team_id>', methods=['PUT'])
def update_team(team_id: int) -> Response:
    content = request.get_json()
    team = Team.create_from_dto(content)
    team_controller.update(team_id, team)
    return make_response("Team updated", HTTPStatus.OK)


@team_bp.route('/<int:team_id>', methods=['PATCH'])
def patch_team(team_id: int) -> Response:
    content = request.get_json()
    team_controller.patch(team_id, content)
    return make_response("Team updated", HTTPStatus.OK)


@team_bp.route('/<int:team_id>', methods=['DELETE'])
def delete_team(team_id: int) -> Response:
    team_controller.delete(team_id)
    return make_response("Team deleted", HTTPStatus.OK)
