import argparse
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import defaultdict
sns.set(style="darkgrid")

import scipy as sp
import scipy.stats

def collect_experiment_data(source='/', runs=1, servers=1, agents=3,hfo=True,compact=False):
    # load all agent data
    evalGoalPercentages = defaultdict(list)
    evalGoalTimes = defaultdict(list)
    evalUsedBudgets = defaultdict(list)
    evalReward = defaultdict(list)
    evalSteps = defaultdict(list)
    evalTrials = np.array([])
    '''
    trainTrials = np.array([])
    trainFrames = defaultdict(list)
    trainScores = defaultdict(list)
    trainUsedBudgets = defaultdict(list)
    '''

    goodRuns = 0
    for server in range(servers):
        for agent in range(1, agents+1):
            for run in range(0, runs):
                evalFile = os.path.join(source, "_"+ str(server) +"_"+ str(run+1) +"_AGENT_"+ str(agent) +"_RESULTS_eval")
                #print evalFile
                if os.path.isfile(evalFile):
                    if(hfo): #HFO experiment
                        try:
                            if compact:
                                _et, _egp, _egt, _eub = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                            else:
                                _et, _egp, _egt, _eub, _er = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                        except:
                            continue
                        if sum(evalTrials)==0:
                            evalTrials = _et
                        #print(sum(_eub.shape), sum(evalTrials.shape))
                        if sum(_eub.shape) == sum(evalTrials.shape):
                            goodRuns += 1
                            for trial in _et:
                                evalGoalPercentages[(agent,trial)].append(_egp)
                                evalGoalTimes[(agent,trial)].append(_egt)
                                evalUsedBudgets[(agent,trial)].append(_eub)
                                if not compact:
                                    evalReward[(agent,trial)].append(_er)
                        else:
                            print("Error " + str(run+1) + " - "+ str(sum(_eub.shape))+" , "+str(sum(evalTrials.shape)))
                    else:
                        #try:
                        _et, _es, _eub = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                        #except:
                        #    continue
                        if sum(evalTrials)==0:
                            evalTrials = _et
                        #print(sum(_eub.shape), sum(evalTrials.shape))
                        if sum(_eub.shape) == sum(evalTrials.shape):
                            goodRuns += 1
                            for trial in _et:
                                evalSteps[(agent,trial)].append(_es)                                
                                evalUsedBudgets[(agent,trial)].append(_eub)
                        else:
                            print("Error " + str(run+1) + " - "+ str(sum(_eub.shape))+" , "+str(sum(evalTrials.shape)))
    goodRuns = int(goodRuns / agents)
    print('Could use %d runs from expected %d' % (goodRuns, runs)) 
    '''
                trainFile = os.path.join(source, "_"+ str(run) +"_"+ str(server) +"_AGENT_"+ str(agent) +"_RESULTS_train")
                print trainFile
                _tt, _tf, _ts, _tub = np.loadtxt(open(trainFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                if sum(trainTrials)==0:
                    trainTrials = _tt
                for trial in _tt:
                    trainFrames[(agent,trial)].append(_tf)
                    trainScores[(agent,trial)].append(_ts)
                    trainUsedBudgets[(agent,trial)].append(_tub)

    for agent in range(1, agents+1):
        for trial in evalTrials:
            # build summaries
            evalGoalPercentages[(agent,trial)] = [summarize_data(evalGoalPercentages[(agent,trial)])]
            evalGoalTimes[(agent,trial)] = [summarize_data(evalGoalTimes[(agent,trial)])]
            evalUsedBudgets[(agent,trial)] = [summarize_data(evalUsedBudgets[(agent,trial)])]
        for trial in trainTrials:
            # build summaries
            trainFrames[(agent,trial)] = [summarize_data(trainFrames[(agent,trial)])]
            trainScores[(agent,trial)] = [summarize_data(trainScores[(agent,trial)])]
            trainUsedBudgets[(agent,trial)] = [summarize_data(trainUsedBudgets[(agent,trial)])]
        '''

    #print('len(evalGoalPercentages) %d --> %s %s' % (len(evalGoalPercentages), str(type(evalGoalPercentages[(1,20)])), str(evalGoalPercentages[(1,20)]) ))
    #print('len(evalGoalTimes) %d --> %s %s' % (len(evalGoalTimes), str(type(evalGoalTimes[(1,20)])), str(evalGoalTimes[(1,20)]) ))
    print('len(evalUsedBudgets) %d --> %s %s' % (len(evalUsedBudgets), str(type(evalUsedBudgets[(1,20)])), str(len(evalUsedBudgets[(1,10)])) ))


    headerLine = []
    headerLine.append("Trial")
    for run in range(1, runs+1):
        headerLine.append("Run"+str(run))

    if(hfo):
        with open(os.path.join(source, "__EVAL_goalpercentages"), 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow((headerLine))
            csvfile.flush()
            for i in range(sum(evalTrials.shape)):
                newrow = [evalTrials[i]]
                for j in evalGoalPercentages[(1,evalTrials[i])]:
                    newrow.append("{:.2f}".format(j[i]))
                csvwriter.writerow((newrow))
                csvfile.flush()
    
        with open(os.path.join(source, "__EVAL_goaltimes"), 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow((headerLine))
            csvfile.flush()
            for i in range(sum(evalTrials.shape)):
                newrow = [evalTrials[i]]
                for j in evalGoalTimes[(1,evalTrials[i])]:
                    newrow.append("{:.2f}".format(j[i]))
                csvwriter.writerow((newrow))
                csvfile.flush()
        if not compact:                
            with open(os.path.join(source, "__EVAL_reward"), 'wb') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow((headerLine))
                csvfile.flush()
                for i in range(sum(evalTrials.shape)):
                    newrow = [evalTrials[i]]
                    for j in evalReward[(1,evalTrials[i])]:
                        newrow.append("{:.2f}".format(j[i]))
                    csvwriter.writerow((newrow))
                    csvfile.flush()
    else:
        with open(os.path.join(source, "__EVAL_stepscaptured"), 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow((headerLine))
            csvfile.flush()
            for i in range(sum(evalTrials.shape)):
                newrow = [evalTrials[i]]
                for j in evalSteps[(1,evalTrials[i])]:
                    newrow.append("{:.2f}".format(j[i]))
                csvwriter.writerow((newrow))
                csvfile.flush()

   
    with open(os.path.join(source, "__EVAL_budgets"), 'wb') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow((headerLine))
        csvfile.flush()

        allBudgets = []
        for trial in range(sum(evalTrials.shape)):
            budgetAvg = [0]* (goodRuns)
            for agent in range(1,agents+1):
                for i in range(len(evalUsedBudgets[(agent,evalTrials[trial])])):
                    #try:
                    budgetAvg[i] += evalUsedBudgets[(agent,evalTrials[trial])][i]/agents
                    #except:
                    #    print i, len(evalUsedBudgets[(agent,evalTrials[trial])])
            allBudgets.append(budgetAvg)
        for i in range(sum(evalTrials.shape)):
            newrow = [evalTrials[i]]
            #print allBudgets[i]
            for j in allBudgets[i]:
                #print(i,j[i])
                newrow.append("{:.2f}".format(j[i]))
            csvwriter.writerow((newrow))
            csvfile.flush()
    

def summarize_data(data, confidence=0.9):
    n = len(data)
    m = np.mean(data,axis=0)
    se = scipy.stats.sem(data,axis=0)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return np.asarray([m, m-h, m+h])


def summarize_experiment_data(source,hfo=True,compact=False):
    if hfo:    
        if compact:
            values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets"]
        else:
            values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets","__EVAL_reward"]
    else:
        values = ["__EVAL_stepscaptured", "__EVAL_budgets"]
    #values = ["__EVAL_goalpercentages", "__EVAL_goaltimes"]
    for value in values:
        evalFile = os.path.join(source, value)
        #print(evalFile)
        evalFileContent = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
        trials = evalFileContent[0]
        data = evalFileContent[1:]
        update = summarize_data(data)
        headerLine = []
        headerLine.append("trial")
        headerLine.append("mean")
        headerLine.append("ci_down")
        headerLine.append("ci_up")

        value = value.replace("EVAL","SUMMARY")
        with open(os.path.join(source, value), 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow((headerLine))
            csvfile.flush()

            for i in range(sum(trials.shape)):
                newrow = [trials[i]]
                for j in update.T[i]:
                    newrow.append("{:.2f}".format(j))
                csvwriter.writerow((newrow))
                csvfile.flush()


def draw_graph(source1 = None, name1 = "Algo1", significant1=None,
               source2 = None, name2 = "Algo2",significant2=None,
               source3 = None, name3 = "Algo3",significant3=None,
               source4 = None, name4 = "Algo4",significant4=None,
               source5 = None, name5 = "Algo5",significant5=None,
               source6 = None, name6 = "Algo5",significant6=None,
               what = "__SUMMARY_goalpercentages", ci = True,nCol = 1,
               #Parameters introduced to allow plot control
               xMin = None, xMax = None, yMin=None, yMax=None
               ):
    plt.figure(figsize=(20,6), dpi=300)
    #Background
    plt.gca().set_axis_bgcolor('white')
    plt.grid(True,color='0.8')
    if source1 != None:
        summary1File = os.path.join(source1, what)
        summary1Content = np.loadtxt(open(summary1File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X1 = summary1Content[0]
        Y11, Y12, Y13 = summary1Content[1],summary1Content[2],summary1Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X1, Y11, Y12, facecolor='#7570b3', alpha=0.2)
            plt.fill_between(X1, Y11, Y13, facecolor='#7570b3', alpha=0.2)
        if(not significant1 is None):
           plt.plot(X1,Y11,label=name1, color='#7570b3', linewidth=4.0,markevery=significant1,marker="d",markersize=8)
        else:
            plt.plot(X1,Y11,label=name1, color='#7570b3', linewidth=4.0)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source2 != None:
        summary2File = os.path.join(source2, what)
        summary2Content = np.loadtxt(open(summary2File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X2 = summary2Content[0]
        Y21, Y22, Y23 = summary2Content[1],summary2Content[2],summary2Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X2, Y21, Y22, facecolor='#e7298a', alpha=0.2)
            plt.fill_between(X2, Y21, Y23, facecolor='#e7298a', alpha=0.2)
        if(not significant2 is None):
            plt.plot(X2,Y21,label=name2, color='#e7298a', linewidth=4.0,markevery=significant2,marker="+",markersize=8)
        else:
            plt.plot(X2,Y21,label=name2, color='#e7298a', linewidth=4.0)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source3 != None:
        summary3File = os.path.join(source3, what)
        summary3Content = np.loadtxt(open(summary3File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X3 = summary3Content[0]
        Y31, Y32, Y33 = summary3Content[1],summary3Content[2],summary3Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X3, Y31, Y32, facecolor='#66a61e', alpha=0.2)
            plt.fill_between(X3, Y31, Y33, facecolor='#66a61e', alpha=0.2)
        if(not significant3 is None):
            plt.plot(X3,Y31,label=name3, color='#66a61e', linewidth=4.0,marker="o",markevery=significant3,markersize=8)
        else:
            plt.plot(X3,Y31,label=name3, color='#66a61e', linewidth=4.0)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source4 != None:
        summary4File = os.path.join(source4, what)
        summary4Content = np.loadtxt(open(summary4File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X4 = summary4Content[0]
        Y41, Y42, Y43 = summary4Content[1],summary4Content[2],summary4Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X4, Y41, Y42, facecolor='#e6ab02', alpha=0.2)
            plt.fill_between(X4, Y41, Y43, facecolor='#e6ab02', alpha=0.2)
        if(not significant4 is None):
            plt.plot(X4,Y41,label=name4, color='#e6ab02', linewidth=4.0,markevery=significant4,marker="H",markersize=8)
        else:
            plt.plot(X4,Y41,label=name4, color='#e6ab02', linewidth=4.0)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source5 != None:
        summary5File = os.path.join(source5, what)
        summary5Content = np.loadtxt(open(summary5File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X5 = summary5Content[0]
        Y51, Y52, Y53 = summary5Content[1],summary5Content[2],summary5Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X5, Y51, Y52, facecolor='black', alpha=0.2)
            plt.fill_between(X5, Y51, Y53, facecolor='black', alpha=0.2)
        if(not significant5 is None):
            plt.plot(X5,Y51,label=name5, color='black', linewidth=4.0,markevery=significant5,marker="x",markersize=8)
        else:
            plt.plot(X5,Y51,label=name5, color='black', linewidth=4.0)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
            
    if source6 != None:
        summary6File = os.path.join(source6, what)
        summary6Content = np.loadtxt(open(summary6File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X6 = summary6Content[0]
        Y61, Y62, Y63 = summary6Content[1],summary6Content[2],summary6Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X6, Y61, Y62, facecolor='black', alpha=0.2)
            plt.fill_between(X6, Y61, Y63, facecolor='black', alpha=0.2)
        if(not significant6 is None):
            plt.plot(X6,Y61,label=name6, color='#999999', linewidth=4.0,markevery=significant6,marker="^",markersize=8)
        else:
            plt.plot(X6,Y61,label=name6, color='#999999', linewidth=4.0)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])

    if what == "__SUMMARY_goalpercentages":
        #plt.title('Goal Percentage per Trial')
        plt.ylabel('Goal %', fontsize=20, fontweight='bold')
    elif what == "__SUMMARY_goaltimes":
        #plt.title('Average Frames to Goal per Trial')
        plt.ylabel('Time to Goal', fontsize=20, fontweight='bold')
    elif what == "__SUMMARY_budgets":
        #plt.title('Used Budget per Trial')
        plt.ylabel('Budget', fontsize=20, fontweight='bold')
    elif what == "__SUMMARY_stepscaptured":
        #plt.title('Used Budget per Trial')
        plt.ylabel('Steps until captured', fontsize=20, fontweight='bold')
    else:
        #plt.title('Unknown')
        plt.ylabel('Unknown')

    plt.xlabel('Training Episodes', fontsize=20, fontweight='bold')
    plt.legend(loc='best',prop={'size':20, 'weight':'bold'},ncol=nCol)
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.show()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--source',default='/home/ruben/playground/HFO/experiments/EVAL/2016_09_12-14.38.02_SARSA_1_5')
    parser.add_argument('-r','--runs',type=int, default=5)
    return parser.parse_args()

def main():
    parameter = get_args()
    collect_experiment_data(parameter.source, runs = parameter.runs)
    summarize_experiment_data(parameter.source)
    #draw_graph(source1=parameter.source)
    #draw_graph(source1=parameter.source, what="__SUMMARY_goaltimes")
    #draw_graph(source1=parameter.source, what="__SUMMARY_budgets")

if __name__ == '__main__':
    main()
