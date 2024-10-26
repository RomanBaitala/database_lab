from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import start_lineup_controller
from ..domain.start_lineup import StartLineup

start_lineup_bp = Blueprint('start_lineup', __name__, url_prefix='/start_lineup')


@start_lineup_bp.route('', methods=['GET'])
def get_all_start_lineups() -> Response:
    return make_response(jsonify(start_lineup_controller.find_all()), HTTPStatus.OK)


@start_lineup_bp.route('', methods=['POST'])
def create_start_lineup() -> Response:
    content = request.get_json()
    start_lineup = StartLineup.create_from_dto(content)
    start_lineup_controller.create(start_lineup)
    return make_response(jsonify(start_lineup.put_into_dto()), HTTPStatus.CREATED)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['GET'])
def get_start_lineup(start_lineup_id: int) -> Response:
    return make_response(jsonify(start_lineup_controller.find_by_id(start_lineup_id)), HTTPStatus.OK)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['PUT'])
def update_start_lineup(start_lineup_id: int) -> Response:
    content = request.get_json()
    start_lineup = StartLineup.create_from_dto(content)
    start_lineup_controller.update(start_lineup_id, start_lineup)
    return make_response("StartLineup updated", HTTPStatus.OK)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['PATCH'])
def patch_start_lineup(start_lineup_id: int) -> Response:
    content = request.get_json()
    start_lineup_controller.patch(start_lineup_id, content)
    return make_response("StartLineup updated", HTTPStatus.OK)


@start_lineup_bp.route('/<int:start_lineup_id>', methods=['DELETE'])
def delete_start_lineup(start_lineup_id: int) -> Response:
    start_lineup_controller.delete(start_lineup_id)
    return make_response("StartLineup deleted", HTTPStatus.OK)
