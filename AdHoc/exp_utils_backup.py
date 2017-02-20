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

def collect_experiment_data(source='/', runs=1, servers=1, agents=3):
    # load all agent data
    evalGoalPercentages = defaultdict(list)
    evalGoalTimes = defaultdict(list)
    evalUsedBudgets = defaultdict(list)
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
                _et, _egp, _egt, _eub = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                if sum(evalTrials)==0:
                    evalTrials = _et
                #print(sum(_eub.shape), sum(evalTrials.shape))
                if sum(_eub.shape) == sum(evalTrials.shape):
                    goodRuns += 1
                    for trial in _et:
                        evalGoalPercentages[(agent,trial)].append(_egp)
                        evalGoalTimes[(agent,trial)].append(_egt)
                        evalUsedBudgets[(agent,trial)].append(_eub)
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


    with open(os.path.join(source, "__EVAL_budgets"), 'wb') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow((headerLine))
        csvfile.flush()

        allBudgets = []
        for trial in range(sum(evalTrials.shape)):
            budgetAvg = [0]* (goodRuns)
            for agent in range(1,agents+1):
                for i in range(len(evalUsedBudgets[(agent,evalTrials[trial])])):
                    budgetAvg[i] += evalUsedBudgets[(agent,evalTrials[trial])][i]/agents
            allBudgets.append(budgetAvg)
        for i in range(sum(evalTrials.shape)):
            newrow = [evalTrials[i]]
            #print allBudgets[i]
            for j in allBudgets[i]:
                #print(i,j[i])
                newrow.append("{:.2f}".format(j[i]))
            csvwriter.writerow((newrow))
            csvfile.flush()


def summarize_data(data, confidence=0.95):
    n = len(data)
    m = np.mean(data,axis=0)
    se = scipy.stats.sem(data,axis=0)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return np.asarray([m, m-h, m+h])


def summarize_experiment_data(source):
    values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets"]
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


def draw_graph(source1 = None, name1 = "Algo1",
               source2 = None, name2 = "Algo2",
               source3 = None, name3 = "Algo3",
               source4 = None, name4 = "Algo4",
               what = "__SUMMARY_goalpercentages", ci = True):
    plt.figure(figsize=(10,6), dpi=80)
    if source1 != None:
        summary1File = os.path.join(source1, what)
        summary1Content = np.loadtxt(open(summary1File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X1 = summary1Content[0]
        Y11, Y12, Y13 = summary1Content[1],summary1Content[2],summary1Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X1, Y11, Y12, facecolor='blue', alpha=0.2)
            plt.fill_between(X1, Y11, Y13, facecolor='blue', alpha=0.2)
        plt.plot(X1,Y11,label=name1, color='blue')
    if source2 != None:
        summary2File = os.path.join(source2, what)
        summary2Content = np.loadtxt(open(summary2File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X2 = summary2Content[0]
        Y21, Y22, Y23 = summary2Content[1],summary2Content[2],summary2Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X2, Y21, Y22, facecolor='green', alpha=0.2)
            plt.fill_between(X2, Y21, Y23, facecolor='green', alpha=0.2)
        plt.plot(X2,Y21,label=name2, color='green')
    if source3 != None:
        summary3File = os.path.join(source3, what)
        summary3Content = np.loadtxt(open(summary3File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X3 = summary3Content[0]
        Y31, Y32, Y33 = summary3Content[1],summary3Content[2],summary3Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X3, Y31, Y32, facecolor='red', alpha=0.2)
            plt.fill_between(X3, Y31, Y33, facecolor='red', alpha=0.2)
        plt.plot(X3,Y31,label=name3, color='red')
    if source4 != None:
        summary4File = os.path.join(source4, what)
        summary4Content = np.loadtxt(open(summary4File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X4 = summary4Content[0]
        Y41, Y42, Y43 = summary4Content[1],summary4Content[2],summary4Content[3]
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X4, Y41, Y42, facecolor='yellow', alpha=0.2)
            plt.fill_between(X4, Y41, Y43, facecolor='yellow', alpha=0.2)
        plt.plot(X4,Y41,label=name4, color='yellow')

    if what == "__SUMMARY_goalpercentages":
        plt.title('Goal Percentage per Trial')
        plt.ylabel('Goal %')
    elif what == "__SUMMARY_goaltimes":
        plt.title('Average Frames to Goal per Trial')
        plt.ylabel('Frames')
    elif what == "__SUMMARY_budgets":
        plt.title('Used Budget per Trial')
        plt.ylabel('Budget')
    else:
        plt.title('Unknown')
        plt.ylabel('Unknown')

    plt.xlabel('Trials')
    plt.legend(loc='upper left')
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
