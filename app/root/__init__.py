from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .referee_route import referee_bp
    from .league_route import league_bp
    from .referee_team_route import referee_team_bp
    from .match_stat_route import match_stat_bp
    from .start_lineup_route import start_lineup_bp
    from .match_route import match_bp
    from .player_route import player_bp
    from .goal_route import goal_bp
    from .team_route import team_bp
    from .stadium_route import stadium_bp
    from .player_stat_route import player_stat_bp
    from .referee_has_referee_team_route import referee_has_referee_team_bp
    from .player_has_start_lineup_route import player_has_start_lineup_bp

    app.register_blueprint(referee_bp)
    app.register_blueprint(league_bp)
    app.register_blueprint(referee_team_bp)
    app.register_blueprint(match_stat_bp)
    app.register_blueprint(start_lineup_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(goal_bp)
    app.register_blueprint(team_bp)
    app.register_blueprint(stadium_bp)
    app.register_blueprint(player_stat_bp)
    app.register_blueprint(referee_has_referee_team_bp)
    app.register_blueprint(player_has_start_lineup_bp)
