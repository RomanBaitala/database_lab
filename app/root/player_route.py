from http import HTTPStatus
from typing import Tuple

from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import player_controller
from ..domain.player import Player, insert_players

player_bp = Blueprint('player', __name__, url_prefix='/player')


@player_bp.route('', methods=['GET'])
def get_all_players() -> Response:
    return make_response(jsonify(player_controller.find_all()), HTTPStatus.OK)


@player_bp.route('', methods=['POST'])
def create_player() -> Response:
    content = request.get_json()
    player = Player.create_from_dto(content)
    player_controller.create(player)
    return make_response(jsonify(player.put_into_dto()), HTTPStatus.CREATED)


@player_bp.route('/<int:player_id>', methods=['GET'])
def get_player(player_id: int) -> Response:
    return make_response(jsonify(player_controller.find_by_id(player_id)), HTTPStatus.OK)


@player_bp.route('/auto_insert', methods=['POST'])
def auto_players_create() -> Response | tuple[Response, int]:
    insert_players()
    return make_response(jsonify({"message": 'Players are created succesfully!'}), HTTPStatus.CREATED)


@player_bp.route('/<int:player_id>', methods=['PUT'])
def update_player(player_id: int) -> Response:
    content = request.get_json()
    player = Player.create_from_dto(content)
    player_controller.update(player_id, player)
    return make_response("Player updated", HTTPStatus.OK)


@player_bp.route('/<int:player_id>', methods=['PATCH'])
def patch_player(player_id: int) -> Response:
    content = request.get_json()
    player_controller.patch(player_id, content)
    return make_response("Player updated", HTTPStatus.OK)


@player_bp.route('/<int:player_id>', methods=['DELETE'])
def delete_player(player_id: int) -> Response:
    player_controller.delete(player_id)
    return make_response("Player deleted", HTTPStatus.OK)
