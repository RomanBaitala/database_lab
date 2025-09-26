from .player_stat_dao import PlayerStatDAO
from .match_stat_dao import MatchStatDAO
from .referee_dao import RefereeDAO
from .start_lineup_dao import StartLineupDAO
from .league_dao import LeagueDAO
from .stadium_dao import StadiumDAO
from .team_dao import TeamDAO
from .referee_team_dao import RefereeTeamDAO
from .match_dao import MatchDAO
from .goal_dao import GoalDAO
from .player_dao import PlayerDAO
from .player_has_start_lineup_dao import PlayerHasStartLineupDAO
from .referee_has_referee_team_dao import RefereeHasRefereeTeamDAO
from .user_dao import UserDAO

player_stat_dao = PlayerStatDAO()
match_stat_dao = MatchStatDAO()
referee_dao = RefereeDAO()
start_lineup_dao = StartLineupDAO()
league_dao = LeagueDAO()
stadium_dao = StadiumDAO()
team_dao = TeamDAO()
referee_team_dao = RefereeTeamDAO()
match_dao = MatchDAO()
goal_dao = GoalDAO()
player_dao = PlayerDAO()
player_has_start_lineup_dao = PlayerHasStartLineupDAO()
referee_has_referee_team_dao = RefereeHasRefereeTeamDAO()
user_dao = UserDAO()
