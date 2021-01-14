<template lang="pug">
.estructura.padding5
    img(src='~static/puntos.png', alt="icon")
    h2.section-title Guide
    section.estructura__derecha.guide
        h4 Submission Format: 
        p The answers should be sended on a .csv file with the following format: A header with (file and emotion). The name of the input file (1224.wav , 1225.wav … )  and the number of the emotion.
        ul 
            li file,emotion
            li 1225.wav,4
            li 1226.wav,4
            li ... 
        h4 Guide: 
        ol 
            li Register on the system
            li Download the dataset files:
            li Train your model using train partition
            li Train your model using train partition
            li Predict the emotions for the Test partition and send your results to the system. The system will evaluate your file and 6. will post your results on the public leaderboard.
            li Predict the emotion for the Challenge partition and send your results. The system will store your results until the deadline. After that, a leaderboard will be posted. And the winners will be announced.





</template>