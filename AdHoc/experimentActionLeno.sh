pkill -f  sh\ ru* 
pkill -f python\ exp*
pkill -f python\ /home/leno/HFO*
killall -9 rcssserver

sh runSimpleExpServer.sh 22445 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgent.sh 22445 AdHocVisitAction 1 5 > log/logAdHocVisitAction.log &

sh runSimpleExpServer.sh 22945 5 > log/serverAdHocTDAction.log &
sleep 5
sh runSimpleExpAgent.sh 22945 AdHocTDAction 6 10 > log/logAdHocTDAction.log &

sh runSimpleExpServer.sh 12445 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgent.sh 12445 AdHocVisitAction 11 15 > log/logAdHocVisitAction.log &

sh runSimpleExpServer.sh 12945 5 > log/serverAdHocTDAction.log &
sleep 5
sh runSimpleExpAgent.sh 12945 AdHocTDAction 16 20 > log/logAdHocTDAction.log &

sh runSimpleExpServer.sh 13445 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgent.sh 13445 AdHocVisitAction 21 25 > log/logAdHocVisitAction.log &

sh runSimpleExpServer.sh 14945 5 > log/serverAdHocTDAction.log &
sleep 5
sh runSimpleExpAgent.sh 14945 AdHocTDAction 26 30 > log/logAdHocTDAction.log &

sh runSimpleExpServer.sh 15445 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgent.sh 15445 AdHocVisitAction 31 35 > log/logAdHocVisitAction.log &

sh runSimpleExpServer.sh 16945 5 > log/serverAdHocTDAction.log &
sleep 5
sh runSimpleExpAgent.sh 16945 AdHocTDAction 36 40 > log/logAdHocTDAction.log &

sh runSimpleExpServer.sh 17445 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgent.sh 17445 AdHocVisitAction 41 45 > log/logAdHocVisitAction.log &

sh runSimpleExpServer.sh 18945 5 > log/serverAdHocTDAction.log &
sleep 5
sh runSimpleExpAgent.sh 18945 AdHocTDAction 46 50 > log/logAdHocTDAction.log &

#sh runSimpleExpServer.sh 22645 32 > log/serverTorreyAction.log &
#sleep 5
#sh runSimpleExpAgent.sh 22645 TorreyAction 19 50 > log/logTorreyAction.log &


