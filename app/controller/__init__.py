from .match_controller import MatchController
from .referee_controller import RefereeController
from .start_lineup_controller import StartLineupController
from .player_stat_controller import PlayerStatController
from .match_stat_controller import MatchStatController
from .referee_team_controller import RefereeTeamController
from .team_controller import TeamController
from .stadium_controller import StadiumController
from .league_controller import LeagueController
from .goal_controller import GoalController
from .player_controller import PlayerController
from .player_has_start_lineup_controller import PlayerHasStartLineupController
from .referee_has_referee_team_controller import RefereeHasRefereeTeamController
from .user_controller import UserController

match_controller = MatchController()
referee_controller = RefereeController()
start_lineup_controller = StartLineupController()
player_stat_controller = PlayerStatController()
match_stat_controller = MatchStatController()
referee_team_controller = RefereeTeamController()
team_controller = TeamController()
stadium_controller = StadiumController()
league_controller = LeagueController()
goal_controller = GoalController()
player_controller = PlayerController()
player_has_start_lineup_controller = PlayerHasStartLineupController()
referee_has_referee_team_controller = RefereeHasRefereeTeamController()
user_controller = UserController()
