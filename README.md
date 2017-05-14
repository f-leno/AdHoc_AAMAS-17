# Simultaneously Learning and Advising in Multiagent Reinforcement Learning

This is the codification used in the AAMAS 2017 paper proposing Ad Hoc Advising as means of accelerating learning in Multiagent Systems composed of simultaneously learning agents. You are free to use all or part of the codes here presented for any purpose, provided that the paper is properly cited and the original authors properly credited. All the files here shared come with no warranties.

Paper bib entry: <br><br>
<i>
 @inproceedings{SilvaAndCosta2017,<br>
  author    = {Silva, Felipe Leno da and <br>
                Ruben Glatt, <br>
  			       Anna Helena Reali Costa},<br>
  title     = {{Simultaneously Learning and Advising in Multiagent Reinforcement Learning}},<br>
  booktitle = {Proceedings of the 16th International Conference on Autonomous Agents and Multiagent Systems (AAMAS)},<br>
    year      = {2017},<br>
    pages = {1100--1108} <br>
    
 }
 </i>
 <br><br>

This project was built on Python 2.7. All the experiments are executed in the HFO platform (https://github.com/LARG/HFO), we included the version we used in the <b>HFO</b> folder (slighly different from the standard HFO). For the graph generation code you will need to install Jupyter Notebook (http://jupyter.readthedocs.io/en/latest/install.html).

# Files
The folder <b>HFO</b> contains the HFO server we used for experiments.

The folder <b>AdHoc</b> contains our implementation of all algorithms and experiments.

Finally, the folder <b>ProcessedFiles</b> contains already processed .csv files for graph printing and data visualization.

# How to use
First install HFO following instructions in https://github.com/LARG/HFO.

In folder <b>AdHoc</b>, executing the script <i>experiment1and2.sh</i> is enough to run the first and second experiment. However, it will take a very long time until the experiments are completed. It may be of interest running more than one algorithm at the same time if you have enough computing power.

Executing <i>experiment3.sh</i> runs the third experiment. Before running this experiment, the script <i>pretrain.sh</i> should be executed, so as to store the Q-table for the already trained agent.

The result of any experiment is a folder with .csv files, that can be used to generate graphs using <i>evaluation-leno.ipynb</i> in jupyter notebook. (all the files used for the paper are in the folder <b>ProcessedFiles</b>).

# Contact

For questions about the Codification or paper, please send an email to the first author.

