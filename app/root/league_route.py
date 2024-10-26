from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import league_controller
from ..domain.league import League

league_bp = Blueprint('league', __name__, url_prefix='/league')


@league_bp.route('', methods=['GET'])
def get_all_leagues() -> Response:
    print('root', league_controller.find_all())
    return make_response(jsonify(league_controller.find_all()), HTTPStatus.OK)


@league_bp.route('', methods=['POST'])
def create_league() -> Response:
    content = request.get_json()
    league = League.create_from_dto(content)
    league_controller.create(league)
    return make_response(jsonify(league.put_into_dto()), HTTPStatus.CREATED)


@league_bp.route('/<int:league_id>', methods=['GET'])
def get_league(league_id: int) -> Response:
    return make_response(jsonify(league_controller.find_by_id(league_id)), HTTPStatus.OK)


@league_bp.route('/<int:league_id>', methods=['PUT'])
def update_league(league_id: int) -> Response:
    content = request.get_json()
    league = League.create_from_dto(content)
    league_controller.update(league_id, league)
    return make_response("League updated", HTTPStatus.OK)


@league_bp.route('/<int:league_id>', methods=['PATCH'])
def patch_league(league_id: int) -> Response:
    content = request.get_json()
    league_controller.patch(league_id, content)
    return make_response("League updated", HTTPStatus.OK)


@league_bp.route('/<int:league_id>', methods=['DELETE'])
def delete_league(league_id: int) -> Response:
    league_controller.delete(league_id)
    return make_response("League deleted", HTTPStatus.OK)
