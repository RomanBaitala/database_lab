from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import referee_controller
from ..domain.referee import Referee

referee_bp = Blueprint('referee', __name__, url_prefix='/referee')


@referee_bp.get('')
def get_all_referees() -> Response:
    return make_response(jsonify(referee_controller.find_all()), HTTPStatus.OK)


@referee_bp.post('')
def create_referee() -> Response:
    content = request.get_json()
    referee = Referee.create_from_dto(content)
    referee_controller.create(referee)
    return make_response(jsonify(referee.put_into_dto()), HTTPStatus.CREATED)


@referee_bp.get('/<int:referee_id>')
def get_referee(referee_id: int) -> Response:
    return make_response(jsonify(referee_controller.find_by_id(referee_id)), HTTPStatus.OK)


@referee_bp.put('/<int:referee_id>')
def update_referee(referee_id: int) -> Response:
    content = request.get_json()
    referee = Referee.create_from_dto(content)
    referee_controller.update(referee_id, referee)
    return make_response("Referee updated", HTTPStatus.OK)


@referee_bp.patch('/<int:referee_id>')
def patch_referee(referee_id: int) -> Response:
    content = request.get_json()
    referee_controller.patch(referee_id, content)
    return make_response("Referee updated", HTTPStatus.OK)


@referee_bp.delete('/<int:referee_id>')
def delete_referee(referee_id: int) -> Response:
    referee_controller.delete(referee_id)
    return make_response("Referee deleted", HTTPStatus.OK)
