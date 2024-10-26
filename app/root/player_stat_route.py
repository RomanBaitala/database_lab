from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import player_stat_controller
from ..domain.player_stat import PlayerStat

player_stat_bp = Blueprint('player_stat', __name__, url_prefix='/player_stat')


@player_stat_bp.route('', methods=['GET'])
def get_all_player_stats() -> Response:
    return make_response(jsonify(player_stat_controller.find_all()), HTTPStatus.OK)


@player_stat_bp.route('', methods=['POST'])
def create_player_stat() -> Response:
    content = request.get_json()
    player_stat = PlayerStat.create_from_dto(content)
    player_stat_controller.create(player_stat)
    return make_response(jsonify(player_stat.put_into_dto()), HTTPStatus.CREATED)


@player_stat_bp.route('/<int:player_stat_id>', methods=['GET'])
def get_player_stat(player_stat_id: int) -> Response:
    return make_response(jsonify(player_stat_controller.find_by_id(player_stat_id)), HTTPStatus.OK)


@player_stat_bp.route('/<int:player_stat_id>', methods=['PUT'])
def update_player_stat(player_stat_id: int) -> Response:
    content = request.get_json()
    player_stat = PlayerStat.create_from_dto(content)
    player_stat_controller.update(player_stat_id, player_stat)
    return make_response("PlayerStat updated", HTTPStatus.OK)


@player_stat_bp.route('/<int:player_stat_id>', methods=['PATCH'])
def patch_player_stat(player_stat_id: int) -> Response:
    content = request.get_json()
    player_stat_controller.patch(player_stat_id, content)
    return make_response("PlayerStat updated", HTTPStatus.OK)


@player_stat_bp.route('/<int:player_stat_id>', methods=['DELETE'])
def delete_player_stat(player_stat_id: int) -> Response:
    player_stat_controller.delete(player_stat_id)
    return make_response("PlayerStat deleted", HTTPStatus.OK)
