pkill -f  sh\ ru* 
pkill -f python\ exp*
#pkill -f python\ /home/leno/HFO*
killall -9 rcssserver

# In order to execute this experiment, one agent must be pre-trained. For that, pretrain.sh should be executed first


sh runSimpleExpServer.sh 49455 50 > ./serverTorreyLo.log &
sleep 5
sh runMultipleAlgExp.sh 49455 Torrey Torrey TorreyLoading 1 50 ./agentData/FilesWithTrainedAgent/ 

sh runSimpleExpServer.sh 49455 50 > ./serverAdHocVisitLo.log &
sleep 5
sh runMultipleAlgExp.sh 49455 AdHocVisit AdHocVisit AdHocVisitLoading 1 50 ./agentData/FilesWithTrainedAgent/ 

sh runSimpleExpServer.sh 48455 50 > ./serverAdHocTDLo.log &
sleep 5
sh runMultipleAlgExp.sh 48455 AdHocTD AdHocTD AdHocTDLoading 1 50 ./agentData/FilesWithTrainedAgent/ 

sh runSimpleExpServer.sh 47455 50 > ./serverSarsaTl.log &
sleep 5
sh runMultipleAlgExp.sh 47455 SARSATile SARSATile SARSATileLoading 1 50 ./agentData/FilesWithTrainedAgent/ 

sh runSimpleExpServer.sh 46455 50 > ./serverEpisodeSh.log &
sleep 5
sh runMultipleAlgExp.sh 46455 EpisodeSharing EpisodeSharing EpisodeSharingLoading 1 50 ./agentData/FilesWithTrainedAgent/ 


