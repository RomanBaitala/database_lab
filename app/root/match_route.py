from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import match_controller
from ..domain.match import FMatch

match_bp = Blueprint('match', __name__, url_prefix='/match')


@match_bp.route('', methods=['GET'])
def get_all_matches() -> Response:
    return make_response(jsonify(match_controller.find_all()), HTTPStatus.OK)


@match_bp.route('', methods=['POST'])
def create_match() -> Response:
    content = request.get_json()
    match = FMatch.create_from_dto(content)
    match_controller.create(match)
    return make_response(jsonify(match.put_into_dto()), HTTPStatus.CREATED)


@match_bp.route('/<int:match_id>', methods=['GET'])
def get_match(match_id: int) -> Response:
    return make_response(jsonify(match_controller.find_by_id(match_id)), HTTPStatus.OK)


@match_bp.route('/<int:match_id>', methods=['PUT'])
def update_match(match_id: int) -> Response:
    content = request.get_json()
    match = FMatch.create_from_dto(content)
    match_controller.update(match_id, match)
    return make_response("Match updated", HTTPStatus.OK)


@match_bp.route('/<int:match_id>', methods=['PATCH'])
def patch_match(match_id: int) -> Response:
    content = request.get_json()
    match_controller.patch(match_id, content)
    return make_response("Match updated", HTTPStatus.OK)


@match_bp.route('/<int:match_id>', methods=['DELETE'])
def delete_match(match_id: int) -> Response:
    match_controller.delete(match_id)
    return make_response("Match deleted", HTTPStatus.OK)
