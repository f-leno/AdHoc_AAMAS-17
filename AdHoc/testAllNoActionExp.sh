pkill -f  sh\ ru* 
pkill -f python\ exp*
pkill -f python\ /home/leno/HFO*
killall -9 rcssserver


sh runSimpleExpServer.sh 11111 21 > serverAdHocTD.log &
sleep 5
sh runSimpleExpAgent.sh 11111 AdHocTD 15 35 > logAdHocTD.log &

sh runSimpleExpServer.sh 11311 15 > serverAdHocTD.log &
sleep 5
sh runSimpleExpAgent.sh 11311 AdHocTD 36 50 > logAdHocTD.log &

sh runSimpleExpServer.sh 12111 4 > serverAdHocVisit.log &
sleep 5
sh runSimpleExpAgent.sh 12111 AdHocVisit 7 10 > logAdHocVisit.log &

sh runSimpleExpServer.sh 13111 24 > serverAdHocVisit.log &
sleep 5
sh runSimpleExpAgent.sh 13111 AdHocVisit 17 30 > logAdHocVisit.log &

sh runSimpleExpServer.sh 13311 20 > serverAdHocVisit.log &
sleep 5
sh runSimpleExpAgent.sh 13311 AdHocVisit 31 50 > logAdHocVisit.log &

#sh runSimpleExpServer.sh 13111 41 > serverSARSA.log &
#sleep 5
#sh runSimpleExpAgent.sh 13111 SARSATile 10 50 > logSARSA.log &

sh runSimpleExpServer.sh 14111 21 > serverTorrey.log &
sleep 5
sh runSimpleExpAgent.sh 14111 Torrey 15 35 > logTorrey.log &

sh runSimpleExpServer.sh 14311 15 > serverTorrey.log &
sleep 5
sh runSimpleExpAgent.sh 14311 Torrey 36 50 > logTorrey.log &


sh runSimpleExpServer.sh 15111 19 > serverEpisode.log &
sleep 5
sh runSimpleExpAgent.sh 15111 EpisodeSharing 17 35 > logEpisode.log &

sh runSimpleExpServer.sh 15311 15 > serverEpisode.log &
sleep 5
sh runSimpleExpAgent.sh 15311 EpisodeSharing 36 50 > logEpisode.log &
