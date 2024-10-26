from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import goal_controller
from ..domain.goal import Goal

goal_bp = Blueprint('goal', __name__, url_prefix='/goal')


@goal_bp.route('', methods=['GET'])
def get_all_goals() -> Response:
    return make_response(jsonify(goal_controller.find_all()), HTTPStatus.OK)


@goal_bp.route('', methods=['POST'])
def create_goal() -> Response:
    content = request.get_json()
    goal = Goal.create_from_dto(content)
    goal_controller.create(goal)
    return make_response(jsonify(goal.put_into_dto()), HTTPStatus.CREATED)


@goal_bp.route('/<int:goal_id>', methods=['GET'])
def get_goal(goal_id: int) -> Response:
    return make_response(jsonify(goal_controller.find_by_id(goal_id)), HTTPStatus.OK)


@goal_bp.route('/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id: int) -> Response:
    content = request.get_json()
    goal = Goal.create_from_dto(content)
    goal_controller.update(goal_id, goal)
    return make_response("Goal updated", HTTPStatus.OK)


@goal_bp.route('/<int:goal_id>', methods=['PATCH'])
def patch_goal(goal_id: int) -> Response:
    content = request.get_json()
    goal_controller.patch(goal_id, content)
    return make_response("Goal updated", HTTPStatus.OK)


@goal_bp.route('/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id: int) -> Response:
    goal_controller.delete(goal_id)
    return make_response("Goal deleted", HTTPStatus.OK)
