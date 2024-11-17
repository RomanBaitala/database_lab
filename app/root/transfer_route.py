from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import transfer_controller
from ..domain.transfers import Transfer

transfer_bp = Blueprint('transfer', __name__, url_prefix='/transfer')


@transfer_bp.route('', methods=['GET'])
def get_all_transfers() -> Response:
    return make_response(jsonify(transfer_controller.find_all()), HTTPStatus.OK)


@transfer_bp.route('', methods=['POST'])
def create_transfer() -> Response:
    content = request.get_json()
    transfer = Transfer.create_from_dto(content)
    transfer_controller.create(transfer)
    return make_response(jsonify(transfer.put_into_dto()), HTTPStatus.CREATED)


@transfer_bp.route('/<int:transfer_id>', methods=['GET'])
def get_transfer(transfer_id: int) -> Response:
    return make_response(jsonify(transfer_controller.find_by_id(transfer_id)), HTTPStatus.OK)


@transfer_bp.route('/<int:transfer_id>', methods=['PUT'])
def update_transfer(transfer_id: int) -> Response:
    content = request.get_json()
    team = Transfer.create_from_dto(content)
    transfer_controller.update(transfer_id, team)
    return make_response("Transfer updated", HTTPStatus.OK)


@transfer_bp.route('/<int:transfer_id>', methods=['PATCH'])
def patch_transfer(transfer_id: int) -> Response:
    content = request.get_json()
    transfer_controller.patch(transfer_id, content)
    return make_response("Transfer updated", HTTPStatus.OK)


@transfer_bp.route('/<int:transfer_id>', methods=['DELETE'])
def delete_transfer(team_id: int) -> Response:
    transfer_controller.delete(team_id)
    return make_response("Transfer deleted", HTTPStatus.OK)
