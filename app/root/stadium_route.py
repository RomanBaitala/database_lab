from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import stadium_controller
from ..domain.stadium import Stadium

stadium_bp = Blueprint('stadium', __name__, url_prefix='/stadium')


@stadium_bp.route('', methods=['GET'])
def get_all_stadiums() -> Response:
    return make_response(jsonify(stadium_controller.find_all()), HTTPStatus.OK)


@stadium_bp.route('', methods=['POST'])
def create_stadium() -> Response:
    content = request.get_json()
    stadium = Stadium.create_from_dto(content)
    stadium_controller.create(stadium)
    return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.CREATED)


@stadium_bp.route('/<int:stadium_id>', methods=['GET'])
def get_stadium(stadium_id: int) -> Response:
    return make_response(jsonify(stadium_controller.find_by_id(stadium_id)), HTTPStatus.OK)


@stadium_bp.route('/<int:stadium_id>', methods=['PUT'])
def update_stadium(stadium_id: int) -> Response:
    content = request.get_json()
    stadium = Stadium.create_from_dto(content)
    stadium_controller.update(stadium_id, stadium)
    return make_response("Stadium updated", HTTPStatus.OK)


@stadium_bp.route('/<int:stadium_id>', methods=['PATCH'])
def patch_stadium(stadium_id: int) -> Response:
    content = request.get_json()
    stadium_controller.patch(stadium_id, content)
    return make_response("Stadium updated", HTTPStatus.OK)


@stadium_bp.route('/<int:stadium_id>', methods=['DELETE'])
def delete_stadium(stadium_id: int) -> Response:
    stadium_controller.delete(stadium_id)
    return make_response("Stadium deleted", HTTPStatus.OK)
