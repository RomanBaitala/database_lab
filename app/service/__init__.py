from .match_service import MatchService
from .player_stat_service import PlayerStatService
from .start_lineup_service import StartLineupService
from .match_stat_service import MatchStatService
from .stadium_service import StadiumService
from .league_service import LeagueService
from .player_service import PlayerService
from .referee_team_service import RefereeTeamService
from .referee_service import RefereeService
from .goal_service import GoalService
from .team_service import TeamService
from .player_has_start_lineup_service import PlayerHasStartLineupService
from .referee_has_referee_team_service import RefereeHasRefereeTeamService
from .transfer_service import TransferService

match_service = MatchService()
player_stat_service = PlayerStatService()
start_lineup_service = StartLineupService()
match_stat_service = MatchStatService()
stadium_service = StadiumService()
league_service = LeagueService()
player_service = PlayerService()
referee_team_service = RefereeTeamService()
referee_service = RefereeService()
goal_service = GoalService()
team_service = TeamService()
player_has_start_lineup_service = PlayerHasStartLineupService()
referee_has_referee_team_service = RefereeHasRefereeTeamService()
transfer_service = TransferService()
