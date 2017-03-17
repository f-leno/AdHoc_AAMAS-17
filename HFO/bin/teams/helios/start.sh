#!/bin/bash

HOST="localhost"
port=6000
coach_port=6002

if [ $# -gt 0 ]; then
    HOST=$1
    shift 1
fi

while [ $# -gt 0 ]
do
  case $1 in
    -p|--port)
      if [ $# -lt 2 ]; then
        usage
        exit 1
      fi
      port="${2}"
      shift 1
      ;;

    -P|--coach-port)
      if [ $# -lt 2 ]; then
        usage
        exit 1
      fi
      coach_port="${2}"
      shift 1
      ;;

    *)
      echo 1>&2
      echo "invalid option \"${1}\"." 1>&2
      echo 1>&2
      exit 1
      ;;
  esac

  shift 1
done

BASEDIR=.

#LD_LIBRARY_PATH=${BASEDIR}/local/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=../local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH

teamname="HELIOS2013"
host=$HOST

DIR="."

player="./helios_player"
coach="./helios_coach"
#port=6000
#coach_port=6002

player_conf="./player.conf"
formation_dir="./data/formations"
role_conf="./data/role.conf"
ball_table_file="./data/ball_table.dat"

goalie_position_dir="./data/goalie_position/"
intercept_conf_dir="./data/intercept_probability/"
opponent_data_dir="./data/opponent_data/"

chain_search_method="BestFirstSearch"
evaluator_name="Default"
sirm_evaluator_param_dir="./data/sirm_evaluator/"
max_chain_length="4"
max_evaluate_size="1000"

coach_conf="./coach.conf"
team_graphic="--use_team_graphic on"


common_opt=""
common_opt="${common_opt} -h ${host} -t ${teamname}"
common_opt="${common_opt} --formation-conf-dir ${formation_dir}"
common_opt="${common_opt} --role-conf ${role_conf}"
common_opt="${common_opt} --ball-table ${ball_table_file}"
common_opt="${common_opt} --chain-search-method ${chain_search_method}"
common_opt="${common_opt} --evaluator-name ${evaluator_name}"
common_opt="${common_opt} --max-chain-length ${max_chain_length}"
common_opt="${common_opt} --max-evaluate-size ${max_evaluate_size}"
common_opt="${common_opt} --sirm-evaluator-param-dir ${sirm_evaluator_param_dir}"
common_opt="${common_opt} --goalie-position-dir ${goalie_position_dir}"
common_opt="${common_opt} --intercept-conf-dir ${intercept_conf_dir}"
common_opt="${common_opt} --opponent-data-dir ${opponent_data_dir}"

player_opt="--player-config ${player_conf}"
player_opt="${player_opt} ${common_opt}"
player_opt="${player_opt} -p ${port}"
player_opt="${player_opt} ${fullstate_opt}"

coach_opt="--coach-config ${coach_conf}"
coach_opt="${coach_opt} ${common_opt}"
coach_opt="${coach_opt} -p ${coach_port}"
coach_opt="${coach_opt} ${team_graphic}"


cd $BASEDIR/helios-13Eindhoven
pwd

NUM_PLAYERS=12
echo $NUM_PLAYERS
for ((i=1;i<=$NUM_PLAYERS;i++)); do
    case $i in
	1)
            $player $player_opt -g &
	    sleep 1
            ;;
	12)
            $coach $coach_opt &
            ;;
	*)
            $player $player_opt &
            ;;
    esac
done
