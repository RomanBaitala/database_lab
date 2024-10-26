from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import player_has_start_lineup_controller
from ..domain.player_has_start_lineup import PlayerHasStartLineup

player_has_start_lineup_bp = Blueprint('player_has_start_lineup', __name__, url_prefix='/player_has_start_lineup')


@player_has_start_lineup_bp.route('', methods=['GET'])
def get_all_player_has_start_lineups() -> Response:
    return make_response(jsonify(player_has_start_lineup_controller.find_all()), HTTPStatus.OK)


@player_has_start_lineup_bp.route('', methods=['POST'])
def create_player_has_start_lineup() -> Response:
    content = request.get_json()
    player_has_start_lineup = PlayerHasStartLineup.create_from_dto(content)
    player_has_start_lineup_controller.create(player_has_start_lineup)
    return make_response(jsonify(player_has_start_lineup.put_into_dto()), HTTPStatus.CREATED)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['GET'])
def get_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    return make_response(jsonify(player_has_start_lineup_controller.find_by_id(player_has_start_lineup_id)), HTTPStatus.OK)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['PUT'])
def update_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    content = request.get_json()
    player_has_start_lineup = PlayerHasStartLineup.create_from_dto(content)
    player_has_start_lineup_controller.update(player_has_start_lineup_id, player_has_start_lineup)
    return make_response("PlayerHasStartLineup updated", HTTPStatus.OK)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['PATCH'])
def patch_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    content = request.get_json()
    player_has_start_lineup_controller.patch(player_has_start_lineup_id, content)
    return make_response("PlayerHasStartLineup updated", HTTPStatus.OK)


@player_has_start_lineup_bp.route('/<int:player_has_start_lineup_id>', methods=['DELETE'])
def delete_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    player_has_start_lineup_controller.delete(player_has_start_lineup_id)
    return make_response("PlayerHasStartLineup deleted", HTTPStatus.OK)
