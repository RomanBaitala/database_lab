from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from ..controller import goal_controller
from ..domain.goal import Goal

goal_bp = Blueprint('goal', __name__, url_prefix='/goal')


# @goal_bp.route('', methods=['GET'])
# @jwt_required()
# def get_all_goals() -> Response:
#     """
#     Endpoint to get all goals
#     ---
#     tags:
#       - Goal
#     security:
#       - Bearer: []
#     responses:
#       200:
#         description: A list of goals
#         examples:
#           application/json: [{
#             "id": 1,
#             "match_id": 1,
#             "player_id": 1,
#             "player_team_id": 1,
#             "time": 12.5
#           }]
#       401:
#         description: Unauthorized or token has expired
#     """
#     return make_response(jsonify(goal_controller.find_all()), HTTPStatus.OK)


@goal_bp.route('', methods=['POST'])
@jwt_required()
def create_goal() -> Response:
    """
    Endpoint to create a goal instance
    ---
    tags:
      - Goal
    responses:
      201:
        description: A goal instance
        examples:
          application/json: [{
            "id": 1,
            "match_id": 1,
            "player_id": 1,
            "player_team_id": 1,
            "time": 12.5
          }]
    """
    content = request.get_json()
    goal = Goal.create_from_dto(content)
    goal_controller.create(goal)
    return make_response(jsonify(goal.put_into_dto()), HTTPStatus.CREATED)


@goal_bp.route('/<int:goal_id>', methods=['GET'])
@jwt_required()
def get_goal(goal_id: int) -> Response:
    """
    Get a goal by ID
    ---
    tags:
      - Goal
    parameters:
      - in: path
        name: goal_id
        type: integer
        required: true
        description: ID of the goal
    responses:
      200:
        description: Goal found
        examples:
          application/json: {"id": 1, "match_id": 1, "player_id": 1, "player_team_id": 1, "time": 12.5}
    """
    return make_response(jsonify(goal_controller.find_by_id(goal_id)), HTTPStatus.OK)


@goal_bp.route('/<int:goal_id>', methods=['PUT'])
@jwt_required()
def update_goal(goal_id: int) -> Response:
    """
        Update a goal by ID
        ---
        tags:
          - Goal
        consumes:
          - application/json
        parameters:
          - in: path
            name: goal_id
            type: integer
            required: true
            description: ID of the goal to update
          - in: body
            name: goal
            required: true
            schema:
              type: object
              properties:
                match_id:
                  type: integer
                player_id:
                  type: integer
                player_team_id:
                  type: integer
                time:
                  type: number
                  format: float
              required:
                - match_id
                - player_id
                - player_team_id
                - time
              example:
                match_id: 1
                player_id: 1
                player_team_id: 1
                time: 12.5
        responses:
          200:
            description: Goal updated successfully
            examples:
              application/json: "Goal updated"
        """
    content = request.get_json()
    goal = Goal.create_from_dto(content)
    goal_controller.update(goal_id, goal)
    return make_response("Goal updated", HTTPStatus.OK)


@goal_bp.route('/<int:goal_id>', methods=['PATCH'])
@jwt_required()
def patch_goal(goal_id: int) -> Response:
    """
    Partially update a goal by ID
    ---
    tags:
      - Goal
    consumes:
      - application/json
    parameters:
      - in: path
        name: goal_id
        type: integer
        required: true
        description: ID of the goal to update
      - in: body
        name: goal
        required: true
        schema:
          type: object
          properties:
            match_id:
              type: integer
            player_id:
              type: integer
            player_team_id:
              type: integer
            time:
              type: number
              format: float
          example:
            match_id: 1
            time: 15.2
    responses:
      200:
        description: Goal updated successfully
        examples:
          application/json: "Goal updated"
    """
    content = request.get_json()
    goal_controller.patch(goal_id, content)
    return make_response("Goal updated", HTTPStatus.OK)


@goal_bp.route('/<int:goal_id>', methods=['DELETE'])
@jwt_required()
def delete_goal(goal_id: int) -> Response:
    """
    Delete a goal by ID
    ---
    tags:
      - Goal
    parameters:
      - in: path
        name: goal_id
        type: integer
        required: true
        description: ID of the goal to delete
    responses:
      200:
        description: Goal deleted successfully
        examples:
          application/json: "Goal deleted"
      404:
        description: Goal not found
        examples:
          application/json: {"error": "Goal not found"}
    """
    goal_controller.delete(goal_id)
    return make_response("Goal deleted", HTTPStatus.OK)
