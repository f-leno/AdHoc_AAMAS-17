#pkill -f  sh\ ru* 
#pkill -f python\ exp*
#pkill -f python\ /home/leno/HFO*
#killall -9 rcssserver

sh runSimpleExpServer.sh 22445 35 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgent.sh 22445 AdHocVisitAction 16 50 > log/logAdHocVisitAction.log &

sh runSimpleExpServer.sh 22945 33 > log/serverAdHocTDAction.log &
sleep 5
sh runSimpleExpAgent.sh 22945 AdHocTDAction 18 50 > log/logAdHocTDAction.log &

#sh runSimpleExpServer.sh 22645 32 > log/serverTorreyAction.log &
#sleep 5
#sh runSimpleExpAgent.sh 22645 TorreyAction 19 50 > log/logTorreyAction.log &


