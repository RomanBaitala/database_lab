from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import match_stat_controller
from ..domain.match_stat import MatchStat

match_stat_bp = Blueprint('match_stat', __name__, url_prefix='/match_stat')


@match_stat_bp.route('', methods=['GET'])
def get_all_match_stats() -> Response:
    """
    Get all match stats
    ---
    tags:
      - MatchStat
    responses:
      200:
        description: A list of match stats
        examples:
          application/json: [
            {
              "id": 1,
              "goals": 3,
              "match_id": 1,
              "possession": 57.5,
              "red_card": 0,
              "yellow_card": 2
            }
          ]
    """
    return make_response(jsonify(match_stat_controller.find_all()), HTTPStatus.OK)


@match_stat_bp.route('', methods=['POST'])
def create_match_stat() -> Response:
    """
    Create a new match stat
    ---
    tags:
      - MatchStat
    requestBody:
      required: true
      content:
        application/json:
          example:
            goals: 3
            match_id: 1
            possession: 57.5
            red_card: 0
            yellow_card: 2
    responses:
      201:
        description: Match stat created successfully
        examples:
          application/json: {
            "id": 1,
            "goals": 3,
            "match_id": 1,
            "possession": 57.5,
            "red_card": 0,
            "yellow_card": 2
          }
    """
    content = request.get_json()
    match_stat = MatchStat.create_from_dto(content)
    match_stat_controller.create(match_stat)
    return make_response(jsonify(match_stat.put_into_dto()), HTTPStatus.CREATED)


@match_stat_bp.route('/<int:match_stat_id>', methods=['GET'])
def get_match_stat(match_stat_id: int) -> Response:
    """
    Get match stat by ID
    ---
    tags:
      - MatchStat
    parameters:
      - name: match_stat_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: A single match stat
        examples:
          application/json: {
            "id": 1,
            "goals": 3,
            "match_id": 1,
            "possession": 57.5,
            "red_card": 0,
            "yellow_card": 2
          }
      404:
        description: Match stat not found
    """
    return make_response(jsonify(match_stat_controller.find_by_id(match_stat_id)), HTTPStatus.OK)


@match_stat_bp.route('/<int:match_stat_id>', methods=['PUT'])
def update_match_stat(match_stat_id: int) -> Response:
    """
    Update match stat (full update)
    ---
    tags:
      - MatchStat
    parameters:
      - name: match_stat_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    requestBody:
      required: true
      content:
        application/json:
          example:
            goals: 3
            match_id: 1
            possession: 57.5
            red_card: 0
            yellow_card: 2
    responses:
      200:
        description: Match stat updated successfully
        examples:
          application/json: "MatchStat updated"
      404:
        description: Match stat not found
    """
    content = request.get_json()
    match_stat = MatchStat.create_from_dto(content)
    match_stat_controller.update(match_stat_id, match_stat)
    return make_response("MatchStat updated", HTTPStatus.OK)


@match_stat_bp.route('/<int:match_stat_id>', methods=['PATCH'])
def patch_match_stat(match_stat_id: int) -> Response:
    """
    Update match stat (partial update)
    ---
    tags:
      - MatchStat
    parameters:
      - name: match_stat_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    requestBody:
      required: true
      content:
        application/json:
          example:
            possession: 60.0
            yellow_card: 3
    responses:
      200:
        description: Match stat partially updated
        examples:
          application/json: "MatchStat updated"
      404:
        description: Match stat not found
    """
    content = request.get_json()
    match_stat_controller.patch(match_stat_id, content)
    return make_response("MatchStat updated", HTTPStatus.OK)


@match_stat_bp.route('/<int:match_stat_id>', methods=['DELETE'])
def delete_match_stat(match_stat_id: int) -> Response:
    """
    Delete match stat by ID
    ---
    tags:
      - MatchStat
    parameters:
      - name: match_stat_id
        in: path
        required: true
        schema:
          type: integer
          example: 1
    responses:
      200:
        description: Match stat deleted
        examples:
          application/json: "MatchStat deleted"
      404:
        description: Match stat not found
    """
    match_stat_controller.delete(match_stat_id)
    return make_response("MatchStat deleted", HTTPStatus.OK)
