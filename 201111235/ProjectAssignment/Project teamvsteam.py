# coding: utf-8
import os
home=os.path.expanduser("~")
import findspark
findspark.init(os.path.join(home,"Downloads","spark-2.0.0-bin-hadoop2.6"))
import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:/Users/DongkyuShin/Desktop/sbigdata/s_201111235/201111235/ProjectAssignment').getOrCreate()

import os
import sys
os.environ["SPARK_HOME"]=os.path.join(os.path.expanduser("~"),'Downloads','spark-2.0.0-bin-hadoop2.6')
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

from pyspark.sql import Row
import numpy as np
import matplotlib.pyplot as plt

team=[None]*2
vsodd=[None]*2
print ("Insert Tow Team.")
for i in range(0,2):
    team[i]=raw_input("")
for a in range(0,2):
    if team[a]=='tottenham':
        cfile= os.path.join(os.path.expanduser("~"),\
                   "Desktop/bigdata/s_201111235/201111235/bigdata/data/tottenham/playerlist.txt")
        rdd = spark.sparkContext.textFile(cfile)
        parts = rdd.map(lambda x:x.split("\t"))
        player = parts.map(lambda p: Row(PlayerNumber=int(p[0].strip()),Name=p[1],Atrribute=int(p[2].strip()),Goal=int(p[3].strip()),Win=int(p[4].strip()), Lose=int(p[5].strip()),Play=int(p[6].strip()),Winper=float(p[7].strip())))

        tDf = spark.createDataFrame(player)

        _atrributeRdd=tDf.rdd.map(lambda fields:fields[0]).collect()
        _goalRdd=tDf.rdd.map(lambda fields:fields[1]).collect()
        _loseRdd=tDf.rdd.map(lambda fields:fields[2]).collect()
        _nameRdd=tDf.rdd.map(lambda fields:fields[3]).collect()
        _playRdd=tDf.rdd.map(lambda fields:fields[4]).collect()
        _numberRdd=tDf.rdd.map(lambda fields:fields[5]).collect()
        _winRdd=tDf.rdd.map(lambda fields:fields[6]).collect()
        _winperRdd=tDf.rdd.map(lambda fields:fields[7]).collect()


        value=[None]*11
        odd=0
        print ("-------------------------------------------------------------------")
        print ("They are currently playing at EPL.")
        print ("PlayerNumber, PlayerName, Goal, Number of Wins, Number of Losses.")
        for i in range(0,23):
            print np.array(_numberRdd)[i],np.array(_nameRdd)[i],np.array(_goalRdd)[i],np.array(_winRdd)[i],np.array(_loseRdd)[i]
        print ("-------------------------------------------------------------------")

        def barchart(data,labels):
            num_bars = len(data)
            positions = range(1, num_bars + 1)
            plt.barh(positions, data, align='center')
            plt.yticks(positions, labels)
            plt.xlabel('Win Odd')
            plt.ylabel('Player')
            plt.title('Number of players won per player')
            plt.grid()
            plt.show()

        barchart(_winperRdd,_nameRdd)
        ##그래프 표현
        print ("Please enter 11 player numbers.")
        for i in range(0,11):
            playerselect=input("")
            value[i]=playerselect
        print ("-------------------------------------------------------------------")
        print ("The odds of the selected player.")

        for i in range(0,11):
            for j in range(0,23):
                if value[i]==np.array(_numberRdd)[j]:
                    odd=odd+float(np.array(_winperRdd)[i])
                    print np.array(_nameRdd)[i],np.array(_numberRdd)[i],np.array(_winperRdd)[i],"%"



        oddsum=odd/11
        vsodd[a]=float(oddsum)

        print ("-------------------------------------------------------------------")
        print ("The odds average of 11 players.")
        print oddsum,"%"
        print ("-------------------------------------------------------------------")

        odd=0
        oddsum=0

    elif team[a]=='arsenal':
        cfile= os.path.join(os.path.expanduser("~"),\
                   "Desktop/bigdata/s_201111235/201111235/bigdata/data/arsenal/playerlist.txt")
        rdd = spark.sparkContext.textFile(cfile)
        parts = rdd.map(lambda x:x.split("\t"))
        player = parts.map(lambda p: Row(PlayerNumber=int(p[0].strip()),Name=p[1],Atrribute=int(p[2].strip()),Goal=int(p[3].strip()),Win=int(p[4].strip()), Lose=int(p[5].strip()),Play=int(p[6].strip()),Winper=float(p[7].strip())))

        tDf = spark.createDataFrame(player)

        _atrributeRdd=tDf.rdd.map(lambda fields:fields[0]).collect()
        _goalRdd=tDf.rdd.map(lambda fields:fields[1]).collect()
        _loseRdd=tDf.rdd.map(lambda fields:fields[2]).collect()
        _nameRdd=tDf.rdd.map(lambda fields:fields[3]).collect()
        _playRdd=tDf.rdd.map(lambda fields:fields[4]).collect()
        _numberRdd=tDf.rdd.map(lambda fields:fields[5]).collect()
        _winRdd=tDf.rdd.map(lambda fields:fields[6]).collect()
        _winperRdd=tDf.rdd.map(lambda fields:fields[7]).collect()


        value=[None]*11
        odd=0
        print ("-------------------------------------------------------------------")
        print ("They are currently playing at EPL.")
        print ("PlayerNumber, PlayerName, Goal, Number of Wins, Number of Losses.")
        for i in range(0,25):
            print np.array(_numberRdd)[i],np.array(_nameRdd)[i],np.array(_goalRdd)[i],np.array(_winRdd)[i],np.array(_loseRdd)[i]
        print ("-------------------------------------------------------------------")

        def barchart(data,labels):
            num_bars = len(data)
            positions = range(1, num_bars + 1)
            plt.barh(positions, data, align='center')
            plt.yticks(positions, labels)
            plt.xlabel('Win Odd')
            plt.ylabel('Player')
            plt.title('Number of players won per player')
            plt.grid()
            plt.show()

        barchart(_winperRdd,_nameRdd)
        ##그래프 표현
        print ("Please enter 11 player numbers.")
        for i in range(0,11):
            playerselect=input("")
            value[i]=playerselect
        print ("-------------------------------------------------------------------")
        print ("The odds of the selected player.")

        for i in range(0,11):
            for j in range(0,25):
                if value[i]==np.array(_numberRdd)[j]:
                    odd=odd+float(np.array(_winperRdd)[i])
                    print np.array(_nameRdd)[i],np.array(_numberRdd)[i],np.array(_winperRdd)[i],"%"



        oddsum=odd/11
        vsodd[a]=float(oddsum)

        print ("-------------------------------------------------------------------")
        print ("The odds average of 11 players.")
        print oddsum,"%"
        print ("-------------------------------------------------------------------")

        odd=0
        oddsum=0
    elif team[a]=='manchestercity':
        cfile= os.path.join(os.path.expanduser("~"),\
                   "Desktop/bigdata/s_201111235/201111235/bigdata/data/manchestercity/playerlist.txt")
        rdd = spark.sparkContext.textFile(cfile)
        parts = rdd.map(lambda x:x.split("\t"))
        player = parts.map(lambda p: Row(PlayerNumber=int(p[0].strip()),Name=p[1],Atrribute=int(p[2].strip()),Goal=int(p[3].strip()),Win=int(p[4].strip()), Lose=int(p[5].strip()),Play=int(p[6].strip()),Winper=float(p[7].strip())))

        tDf = spark.createDataFrame(player)

        _atrributeRdd=tDf.rdd.map(lambda fields:fields[0]).collect()
        _goalRdd=tDf.rdd.map(lambda fields:fields[1]).collect()
        _loseRdd=tDf.rdd.map(lambda fields:fields[2]).collect()
        _nameRdd=tDf.rdd.map(lambda fields:fields[3]).collect()
        _playRdd=tDf.rdd.map(lambda fields:fields[4]).collect()
        _numberRdd=tDf.rdd.map(lambda fields:fields[5]).collect()
        _winRdd=tDf.rdd.map(lambda fields:fields[6]).collect()
        _winperRdd=tDf.rdd.map(lambda fields:fields[7]).collect()


        value=[None]*11
        odd=0
        print ("-------------------------------------------------------------------")
        print ("They are currently playing at EPL.")
        print ("PlayerNumber, PlayerName, Goal, Number of Wins, Number of Losses.")
        for i in range(0,22):
            print np.array(_numberRdd)[i],np.array(_nameRdd)[i],np.array(_goalRdd)[i],np.array(_winRdd)[i],np.array(_loseRdd)[i]
        print ("-------------------------------------------------------------------")

        def barchart(data,labels):
            num_bars = len(data)
            positions = range(1, num_bars + 1)
            plt.barh(positions, data, align='center')
            plt.yticks(positions, labels)
            plt.xlabel('Win Odd')
            plt.ylabel('Player')
            plt.title('Number of players won per player')
            plt.grid()
            plt.show()

        barchart(_winperRdd,_nameRdd)
        ##그래프 표현
        print ("Please enter 11 player numbers.")
        for i in range(0,11):
            playerselect=input("")
            value[i]=playerselect
        print ("-------------------------------------------------------------------")
        print ("The odds of the selected player.")

        for i in range(0,11):
            for j in range(0,22):
                if value[i]==np.array(_numberRdd)[j]:
                    odd=odd+float(np.array(_winperRdd)[i])
                    print np.array(_nameRdd)[i],np.array(_numberRdd)[i],np.array(_winperRdd)[i],"%"



        oddsum=odd/11
        vsodd[a]=float(oddsum)

        print ("-------------------------------------------------------------------")
        print ("The odds average of 11 players.")
        print oddsum,"%"
        print ("-------------------------------------------------------------------")

        odd=0
        oddsum=0

    elif team[a]=='chelsea':
        cfile= os.path.join(os.path.expanduser("~"),\
                   "Desktop/bigdata/s_201111235/201111235/bigdata/data/chelsea/playerlist.txt")
        rdd = spark.sparkContext.textFile(cfile)
        parts = rdd.map(lambda x:x.split("\t"))
        player = parts.map(lambda p: Row(PlayerNumber=int(p[0].strip()),Name=p[1],Atrribute=int(p[2].strip()),Goal=int(p[3].strip()),Win=int(p[4].strip()), Lose=int(p[5].strip()),Play=int(p[6].strip()),Winper=float(p[7].strip())))

        tDf = spark.createDataFrame(player)

        _atrributeRdd=tDf.rdd.map(lambda fields:fields[0]).collect()
        _goalRdd=tDf.rdd.map(lambda fields:fields[1]).collect()
        _loseRdd=tDf.rdd.map(lambda fields:fields[2]).collect()
        _nameRdd=tDf.rdd.map(lambda fields:fields[3]).collect()
        _playRdd=tDf.rdd.map(lambda fields:fields[4]).collect()
        _numberRdd=tDf.rdd.map(lambda fields:fields[5]).collect()
        _winRdd=tDf.rdd.map(lambda fields:fields[6]).collect()
        _winperRdd=tDf.rdd.map(lambda fields:fields[7]).collect()


        value=[None]*11
        odd=0
        print ("-------------------------------------------------------------------")
        print ("They are currently playing at EPL.")
        print ("PlayerNumber, PlayerName, Goal, Number of Wins, Number of Losses.")
        for i in range(0,20):
            print np.array(_numberRdd)[i],np.array(_nameRdd)[i],np.array(_goalRdd)[i],np.array(_winRdd)[i],np.array(_loseRdd)[i]
        print ("-------------------------------------------------------------------")

        def barchart(data,labels):
            num_bars = len(data)
            positions = range(1, num_bars + 1)
            plt.barh(positions, data, align='center')
            plt.yticks(positions, labels)
            plt.xlabel('Win Odd')
            plt.ylabel('Player')
            plt.title('Number of players won per player')
            plt.grid()
            plt.show()

        barchart(_winperRdd,_nameRdd)
        ##그래프 표현
        print ("Please enter 11 player numbers.")
        for i in range(0,11):
            playerselect=input("")
            value[i]=playerselect
        print ("-------------------------------------------------------------------")
        print ("The odds of the selected player.")

        for i in range(0,11):
            for j in range(0,20):
                if value[i]==np.array(_numberRdd)[j]:
                    odd=odd+float(np.array(_winperRdd)[i])
                    print np.array(_nameRdd)[i],np.array(_numberRdd)[i],np.array(_winperRdd)[i],"%"



        oddsum=odd/11
        vsodd[a]=float(oddsum)

        print ("-------------------------------------------------------------------")
        print ("The odds average of 11 players.")
        print oddsum,"%"
        print ("-------------------------------------------------------------------")

        odd=0
        oddsum=0






print team[0],("vs"),team[1],(":"),vsodd[0],"%",("vs"),vsodd[1],("%"),("\n")
