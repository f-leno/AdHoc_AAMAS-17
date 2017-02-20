#!/bin/bash

echo "[$(date +"%Y-%m-%d_%H:%M:%S")] RUNNING HFO EXPERIMENT"
echo "[$(date +"%Y-%m-%d_%H:%M:%S")] PARSING ARGUMENTS"

for i in "$@"
do
  case $i in
    -r=*|--runs=*)
    RUNS="${i#*=}"
    shift
    ;;
    -t=*|--trials=*)
    TRIALS="${i#*=}"
    shift
    ;;
    -f=*|--max-frames-per-trial=*)
    MAX_FRAMES="${i#*=}"
    shift
    ;;
    -a=*|--agent=*)
    AGENT="${i#*=}"
    shift
    ;;
    -o=*|--offense-agents=*)
    OFFENSE_AGENTS="${i#*=}"
    shift
    ;;
    -d=*|--defense-agents=*)
    DEFENSE_AGENTS="${i#*=}"
    shift
    ;;
    -m=*|--mode=*)
    MODE="${i#*=}"
    shift
    ;;
    -i=*|--evaluation_interval=*)
    INTERVAL="${i#*=}"
    shift
    ;;
    -e=*|--evaluation_duration=*)
    DURATION="${i#*=}"
    shift
    ;;
  esac
  shift
done

if [ -z "${RUNS+x}" ]; then
  RUNS=1
fi
if [ -z "${TRIALS+x}" ]; then
  TRIALS=10
fi
if [ -z "${MAX_FRAMES+x}" ]; then
  MAX_FRAMES=100
fi
if [ -z "${AGENT+x}" ]; then
  AGENT="Dummy"
fi
if [ -z "${OFFENSE_AGENTS+x}" ]; then
  OFFENSE_AGENTS=2
fi
if [ -z "${DEFENSE_AGENTS+x}" ]; then
  DEFENSE_AGENTS=0
fi
if [ -z "${MODE+x}" ]; then
  MODE="--no-sync"
  # headless, no-sync (watching in slow pace),
fi
if [ -z "${INTERVAL+x}" ]; then
  INTERVAL=5
fi
if [ -z "${DURATION+x}" ]; then
  DURATION=5
fi

#Now the number of trials is incremented to take into account how many
# evaluation trials will be carried out
((EVAL_COUNT=${TRIALS}/${INTERVAL}))
((EVAL_TRIALS=${EVAL_COUNT}*${DURATION}))
((TRIALS_TOTAL=${TRIALS}+${EVAL_TRIALS}))

echo "[$(date +"%Y-%m-%d_%H:%M:%S")] SELECTED PARAMETERS: "\
"RUNS=${RUNS}, TRIALS=${TRIALS}, MAX_FRAMES=${MAX_FRAMES}, AGENT=${AGENT}, "\
"OFFENSE_AGENTS=${OFFENSE_AGENTS}, DEFENSE_AGENTS=${DEFENSE_AGENTS}, "\
"EVAL_TRIALS=${EVAL_TRIALS},INTERVAL=${INTERVAL}, DURATION=${DURATION}, "\
"TRIALS_TOTAL=${TRIALS_TOTAL}"

_now=$(date +"%Y_%m_%d-%H.%M.%S")
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
_dir="${BASE_DIR}/LOGS/${_now}_${AGENT}/"
echo "[$(date +"%Y-%m-%d_%H:%M:%S")] BASE DIRECTORY: ${BASE_DIR}"
echo "[$(date +"%Y-%m-%d_%H:%M:%S")] MAKE LOG DIRECTORY: ${_dir}"

mkdir -p ${_dir};

killall -9 rcssserver

for ((run=1; run<=${RUNS}; run++ ))
do
  echo "[$(date +"%Y-%m-%d_%H:%M:%S")] STARTING RUN ${run} =================="
  echo "[$(date +"%Y-%m-%d_%H:%M:%S")] STARTING HFO SERVER"
  ./bin/HFO \
  --log-dir "${_dir}" \
  --offense-agents "${OFFENSE_AGENTS}" \
  --defense-npcs "${DEFENSE_AGENTS}" \
  --trials "${TRIALS_TOTAL}" \
  --frames-per-trial "${MAX_FRAMES}" \
  --headless \
  --fullstate &
  # instead of headless: --no-sync \

  HFO_PID=$!
  echo "[$(date +"%Y-%m-%d_%H:%M:%S")] HFO SERVER PID: ${HFO_PID}"

  for ((agent=1; agent<=${OFFENSE_AGENTS}; agent++ ))
  do
   sleep 5
    echo "[$(date +"%Y-%m-%d_%H:%M:%S")] STARTING AGENT ${agent}"
    "${BASE_DIR}"/experiment.py -a "${AGENT}" -i "${INTERVAL}" -d \
    "${DURATION}" -t "${TRIALS}" -l "${_dir}${AGENT}"_"${run}"_"${agent}"  &
  done
  wait ${HFO_PID}
  sleep 5
  killall -9 rcssserver
  mv -v "${_dir}"incomplete.hfo "${_dir}"incomplete_"${run}".hfo
done

# The magic line
#   $$ holds the PID for this script
#   Negation means kill by process group id instead of PID
trap "kill -TERM -$$" SIGINT
wait
