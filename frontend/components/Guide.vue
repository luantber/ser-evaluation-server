<template lang="pug">
.estructura.padding5
    img(src='~static/puntos.png', alt="icon")
    h2.section-title Guide and rules
    section.estructura__derecha.guide
        h4 Submission Format: 
        p The answers should be sended on a .csv file with the following format: A header with (file and emotion). The name of the input file (1224.wav , 1225.wav … )  and the number of the emotion.
        ul 
            li file,emotion
            li 1225.wav,4
            li 1226.wav,4
            li ... 

        p The name of the file should follow this format: 
        p "username_dataset_mode.csv" , where 
        ul
            li username is the name or alias of the participant. ( should not contain underscores "_" )
            li dataset: ravdess, kusisqa, iemocap.
            li mode: test, challenge.
        h5 Example: 
        p "lbernal_ravdess_challenge.csv"
        p Send your file to the email: lbernal@unsa.edu.pe with subject "SERChallenge - [participant or team participant name]". 
    
        
        h4 Rules 
        ol
            li Participants must train a machine learning / deep learning model using the proposed audio and labels files.
            li Each day will be published a leaderboard based on the Submissions of the anwsers of test partitions.
            li The leaderboard will include the username of the participant and the score of the result sended ( based in some metrics like F1-score, weighted accuracy, ie)
            li One day after the deadline will be published the final leaderboard based on the last Submission  for challenge dataset. 




        //- h4 Guide: 
        //- ol 
        //-     li Register on the system
        //-     li Download the dataset files:
        //-     li Train your model using train partition
        //-     li Train your model using train partition
        //-     li Predict the emotions for the Test partition and send your results to the system. The system will evaluate your file and 6. will post your results on the public leaderboard.
        //-     li Predict the emotion for the Challenge partition and send your results. The system will store your results until the deadline. After that, a leaderboard will be posted. And the winners will be announced.





</template>