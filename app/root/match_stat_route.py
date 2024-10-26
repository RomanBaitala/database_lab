from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import match_stat_controller
from ..domain.match_stat import MatchStat

match_stat_bp = Blueprint('match_stat', __name__, url_prefix='/match_stat')


@match_stat_bp.route('', methods=['GET'])
def get_all_match_stats() -> Response:
    return make_response(jsonify(match_stat_controller.find_all()), HTTPStatus.OK)


@match_stat_bp.route('', methods=['POST'])
def create_match_stat() -> Response:
    content = request.get_json()
    match_stat = MatchStat.create_from_dto(content)
    match_stat_controller.create(match_stat)
    return make_response(jsonify(match_stat.put_into_dto()), HTTPStatus.CREATED)


@match_stat_bp.route('/<int:match_stat_id>', methods=['GET'])
def get_match_stat(match_stat_id: int) -> Response:
    return make_response(jsonify(match_stat_controller.find_by_id(match_stat_id)), HTTPStatus.OK)


@match_stat_bp.route('/<int:match_stat_id>', methods=['PUT'])
def update_match_stat(match_stat_id: int) -> Response:
    content = request.get_json()
    match_stat = MatchStat.create_from_dto(content)
    match_stat_controller.update(match_stat_id, match_stat)
    return make_response("MatchStat updated", HTTPStatus.OK)


@match_stat_bp.route('/<int:match_stat_id>', methods=['PATCH'])
def patch_match_stat(match_stat_id: int) -> Response:
    content = request.get_json()
    match_stat_controller.patch(match_stat_id, content)
    return make_response("MatchStat updated", HTTPStatus.OK)


@match_stat_bp.route('/<int:match_stat_id>', methods=['DELETE'])
def delete_match_stat(match_stat_id: int) -> Response:
    match_stat_controller.delete(match_stat_id)
    return make_response("MatchStat deleted", HTTPStatus.OK)
