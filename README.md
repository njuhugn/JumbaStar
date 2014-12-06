# Stat 157 - Final Report
=========
## Information
* Author: Sida Ye, Victor Jiang, Jiajun Chen, Jiabin Chen
* Date: 12/05/2014

# Abstract
* In this report, we report the process and the result we have for the KDD Cup 2012 click-through-rate (CTR) prediction of advertisements. To achieve that, we train our data in Naive Bayes, Generalized Linear Model and Gradient Boosting Model. We fitted each of the models with the best features that returned the highest prediction accuracies. For this report, we present the results through each individual model we used.


# Problem Statement
* The goal for this project was to predict click-through-rate and maximize the prediction accuracy. To achieve this goal, we aggregated various features and made different combinations of them. Then we applied three models -- Naive Bayes, GLM and Boosting on the training sets.



# Introduction
* Click-through-rate of advertisement is a major concern for almost all search engines, major websites as well as other internet companies. The accuracy of the prediction determines one company’s profit from advertisements and it directly affects the strategies for the companies to sell their available advertisements. 


# Description of Database
* The data we used is from the KDD cup, held by Soso.com. To train our model, we used training-60.txt, which contained all the information for each instances and it was the main file we used in this project. We also used userid\_profile.txt, which contains the age and gender for each user ID. The last two files are queryid\_tokensid.txt and titleid\_tokensid, which had query ID, title ID and all the tokens ID. 


# Model
--------

##	**Naive Bayes**
###   **Description**
* Naive Bayes are a family of simple probabilistic classifiers based on applying Bayes' theorem with strong independence assumptions between the features. 

###  **Feature**
* Categorical feature: We used the categorical features adid, depth and position in our Naive Bayes  model. We aggregated click and impression for each unique adid


* Categorical feature:
* We used the categorical features ad_id, depth and position in our Naive Bayes  model. We aggregated click and impression for each unique ad_id, position and depth. After that, we combined all the instances for each feature with less than 20 impressions and called them “UNK” to represent the feature not shown up yet. The input data for our Naive Bayes models can be found in S3://stat157-uq85def/home/chenjiajunjerry/final_project/data_aggregate2/output/out2

\smallskip

  \item Similarity feature:\\
We calculated the similarity between queryID token and titleID token. First, we use mapjoin in AWS  to combine querID\_token file, titleID\_token file and train dataset file together, making it as a large file.
The output is on \url{S3: All Bucket/stat157-uq85def/home/clickpn/smiliarity/outputs/out8
}
\begin{enumerate}
  \item 1-token similarity:\\
Based on the large file, we calculated the 1-token similarity by finding the same token in queryID\_token file and titleID\_token file. Then, we divided the number of same tokens by length of queryID\_token.
The output is on \url{S3: All Bucket/stat157-uq85def/home/clickpn/smiliarity/outputs/out9}
  \item 2-token similarity:\\
Based on the large file, we calculated the 2-token similarity by finding the number of two consecutive same tokens in titleID’s token and queryID’s token. Then, we divided the number of 2-token by the length of queryID\_token.
The output is on \url{S3: All Bucket/stat157-uq85def/home/clickpn/smiliarity/outputs/2tokenout}
\end{enumerate}

\smallskip
  \item Gender and age:\\
The UserID consists of age and gender groups. The age\_gender feature is the 12 different groups, from cross between 2 gender groups and 6 age groups. For different genders, the probability of whether to click on an advertisement is different, since males and females are likely to focus on different subjects when shopping, which is also obvious in the real world. Also the same rule applies to different age groups. We can categorize all users to different combinations of ages and genders. The output can be found on \url{S3:
stat157-uq85def/home/chenjiajunjerry/final_project/gender_age/outputs/out1}
 
\smallskip
 \item Relative position:\\
(The relative position, which is $\frac{(depth - pos)} { depth}$., of the advertisements also can affect the CTR. As people usually pay attention on some easy detecting area of screen. If an ad is placed right in the middle and at the beginning, then it might attracts more people to click. We can value different positions to some number rank by their easiness to get access. 
The output is on \url{S3: All Bucket/stat157-uq85def/home/clickpn/relative_pos/outputs/out1}
\end{itemize}


\subsubsection{Procedure}
For this model, we first find the probability of feature equals value given clicked or not clicked. Then we use bayes rule to find our target value: Pr(Click | Data) 
The formula we used in this part is:\\

\vspace*{-10pt}
\textbf{Pr(click \textbar\   feature = value)} = $\frac{Pr(click \ \delta feature==value)}{Pr(feature = value | click)+Pr(feature = value | nonclick)}$ 
\setlength{\parskip}{5 pt}
\smallskip

On top of that, we also did additive smoothing to our sample probability. If the click through rate for one feature value is zero, we will use the following formula: to make adjustment:\\

\vspace*{-8pt}
\textbf{Adjustment Probability} = $\frac{Xi+ \alpha}{N + \alpha*d}$ (i=1,2...d),
\setlength{\parskip}{5 pt}
\smallskip

In order to deal with values that are not in the training set but in the validation set, we aggregated all the entries with impressions less than 20 into one basket “UNK”. When running through the validation set, if we saw some id that is not in the training set, we would just use the probability represented by the UNK entry.\\ 

\vspace*{-8pt}
In the end, we went through each single feature and tried out the combinations of these features to get the highest auc.
\vspace*{-10pt}


\subsubsection{Results/AUC}
The training outcome(sample\_prob.txt) can be found at \url{s3://stat157-uq85def/home/jiangyuhao36/Submission}. And the detailed auc results(out.txt) can be found at \url{S3://stat157-uq85def/home/jiangyuhao36/Submission}. 




\begin{center}
  \begin{tabular}{ l | c | c | c | c | c | c || c }
    \hline
    Comb & ADid & Similarity & Relative-Pos & Historical CTR & Gender-Age & Depth-Pos & AUC \\ \hline
    No.1 & X  &  & & & & & 71.56\% \\ \hline
    No.2 &  &X  & & & & & 56.08\% \\ \hline
    No.3 &  &  &X & & & & 53.27\%  \\ \hline
    No.4 &  &  & &X & & & 71.21\% \\ \hline
    No.5 &  &  & & & X & & 50.36\%  \\ \hline
    No.6 &X  &  &X &X & &X & 73.07\% \\ \hline
    No.7 &X  &X  &X &X & &X & 66.07\% \\
    \hline
  \end{tabular}
\end{center}

\begin{center}
 \textbf{Best AUC we have }

\end{center}

\begin{figure}[ht!]
\centering
\includegraphics[width=90mm]{photo.jpg}
\caption{A simple caption \label{overflow}}
\end{figure}



\subsubsection{Limitation }
In this model, we firstly assumed each feature is independent with each other while in reality, they are not. Therefore the prediction accuracy might not well reflect the model’s theoretical accuracy. The reason that our AUC for similarity is not high is we only calculated the similarity index between queryID and titleID. If we could calculate similarity index between queryID and AdID, which is a combination of titleID, keywordID and descriptionID, our AUC should be much higher than now.











\subsection{GLM}
\subsubsection{Description}
Besides Naive Bayes, we also used generalized linear model to predict click-through-rates. We assumed that the number of click and non-click for each combination of features follows a binomial distribution. We first aggregated the train data then ran it in R. 
\subsubsection{Features}
We only used categorical features ad-id, depth and position in our GLM. We extracted these three features along with the click and impression for each instance to create a data frame. Each column of this data frame corresponded to a different feature and the last two columns were impression and click. We then aggregated this data frame by the uniqueness of feature. The response variables are number of clicks and no-clicks. 
\subsubsection{Procedure}
We did this process on EC2 due to the limitation of our own computers. The factor levels of categorical features had large influence on running the glm function in R. By referring to the lecture 24’s R demo code, we used the ReduceFactorLevel function to reduce the original numbers of ad-id’s levels into 20 levels. To further reduce the data size, we only kept the instance with less than 50 impressions. Then we connected local computer with EC2. In this case, we can get the result in a short time. 
\subsubsection{Results/AUC}
The final AUC we achieved was 10.7\%, which was very low. We believed this is due to the fact that we reduced the ad\_id feature to only 20 levels and we disregarded all the instance with more than 50 impressions in our regression model.
\subsubsection{Limitation}
Due to the lack of memory, we can only apply glm function on ad\_id with 20 different factor levels. Another limitation was that we only included three categorical features and omit other potential variables in our model. These two limitations lower the accuracy in prediction.









\subsection{Boosting(GBM)}
\subsubsection{Description}
The Gradient Boosting Model is a special case of the function gradient descent view of boosting, which is a decision-tree method that grows trees sequentially: each tree is grown using information from previously grown trees.
\subsubsection{Features}
The features in GBM model is the same as those in GLM, which were ad\_id, depth and position.
\subsubsection{Procedure}
To meet the requirement of input data format for the gbm function in R, we first transformed our train dataset into one with non-clicks. We assigned a new column called ‘y’ for each dataset. For original train dataset, we assigned ‘y’ as 1, while for no-click train dataset, we assigned ‘y’ to 0. Meanwhile, we named ‘w’ and assigned values as the weight for further use. We combined the original train dataset and the transformed train dataset together and subsetted with weight greater than 0. By implementing gbm function in gbm R package, we were able to get the results. Also, all these works were done on EC2.  
\subsubsection{Results/AUC}
The final AUC is 50\%, which is not very satisfactory. 


\subsubsection{Limitation}
We believe the small factor level lower our accuracy in prediction. We can not reduce factor levels to 100 instead of 20 due to the lack of memory.








\section{Responsibilities}

The responsibilities  for each of the group member is the following:

\begin{table}[h]\centering
\large
\begin{tabular}{| c | c |}
\hline
Responsibility & Person(s)\\
\hline
Data Aggregation & Jiajun Chen, Sida Ye, Victor Jiang\\
\hline
Developing Features & Sida Ye, Jiajun Chen, Jiabin Chen\\
\hline
Naive Bayes Model & Victor Jiang\\
\hline
GLM & Sida Ye, Jiajun Chen\\
\hline
GBM-Boosting & Sida Ye, Jiajun Chen, Jiabin Chen\\
\hline
Calculating AUC & Victor Jiang\\
\hline
AWS \& Github & Sida Ye, Jiajun Chen, Victor Jiang\\
\hline
Write-up& Together\\
\hline
\end{tabular}\\
\end{table}



\section{Conclusion}
In this report, we specified the models we used and the features we selected in order to get the highest prediction accuracy thus AUC. Since the data sets are quite large, it took very long time to run the data. Among GLM and GBM, we had to reduce some features in order to get the results even in AWS. Therefore the prediction accuracies can be even higher if we did not have such restrictions. 


\section{References}
1. Wu, Kuan-wei; et al.\emph{``A Two-Stage Ensemble of Diverse Models for Advertisement Ranking in KDD Cup 2012."}:  2012. Web.\\
2. Michael Jahrer; et al.\emph{``Ensemble of Collaborative Filtering and Feature Engineered Models for Click Through Rate Prediction."}:  2012. Web.\\


\end{document}  
