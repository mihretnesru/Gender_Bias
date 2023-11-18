#!/usr/bin/env python
# coding: utf-8

class BayesianGenderBias:
    def __init__(self, feminine_coded_words, masculine_coded_words):
        self.feminine_coded_words = feminine_coded_words
        self.masculine_coded_words = masculine_coded_words
        self.p_feminine = None
        self.p_masculine = None

    def train(self, job_descs, labels):
        '''
        prepare training data of different labels
        '''
        label_counts = Counter(labels)
        num_feminine = label_counts["feminine"]
        num_masculine = label_counts["masculine"]
        total_job_descs = len(labels)

        self.p_feminine = num_feminine / total_job_descs
        self.p_masculine = num_masculine / total_job_descs
    def predict(self, job_descs):
        '''
        calculate probabilities of individual classes and store results
        '''

        #### TASK A : tokenize job description to a list of words ###

        '''
            .split() is most basic approach to convers, but you are asked to use more better ways 
            like regular expressions, nlp tools, remove stop words
            job_desc_words = job_desc.split()

            It would be nice if you use Lemmatizer functions.

            '''
        #print(job_descs)

        # spliting words in each job descriptions and removing stop words and punctuation
        jobs=[]
        job_desc_words=[]

        for words in job_descs:
            stop_words = ['have',"are",'a','as',"an", "the", "in", "on", "and", "your",'with','to',
            'if','our',"you're",'be','of','where',"you'll",'that','is','at','you','their']
            translator = str.maketrans('', '', string.punctuation)
            words=words.lower()
            words=words.translate(translator)
            jobs.append(words.split())
      
        for words in jobs:
            job=[]
            for word in words:
                if word not in stop_words:
                  job.append(word)
            job_desc_words.append(job)
        
        #print(job_desc_words)
        
            ############################################################

            # calculate probabilities for each job description
        p_feminine_given_job_desc = self.calculate_p_feminine_given_job_desc(job_desc_words)
        p_masculine_given_job_desc = self.calculate_p_masculine_given_job_desc(job_desc_words)
            
            #### TASK B: Observe the probabilities ###
        
            


            ########################################
        for i in range(len(p_masculine_given_job_desc)):   
            if  p_feminine_given_job_desc[i] > p_masculine_given_job_desc[i]:
                predictions.append("feminine")
            else:
                predictions.append("masculine")
        return predictions

    

    def calculate_p_masculine_given_job_desc(self, job_desc_words):
        '''
            calculate the probability of being masculine given the job_desc
        '''
        p_masculine_given_job_desc = self.p_masculine
        #print(p_masculine_given_job_desc)
        
        #create a masculine list from the job descrpiton
        masculine=[]
        for words in job_desc_words:
            m=[]
            for word in words:
                if word in masculine_coded_words:
                    m.append(word)
            masculine.append(m)
        print(f'masculine words:{masculine}')


        # Counting word frequencies in masculine list
        
        masculine_freq=[]
        for words in masculine:
            masculine_word_count={}
            if len(words)==0:
                masculine_word_count["<no words>"] = 0
            for word in words:
                if word in masculine_word_count:
                    masculine_word_count[word] += 1
                else:
                    masculine_word_count[word] = 1
                
            masculine_freq.append(masculine_word_count)
        print(f'masculine words frequency:{masculine_freq}')

        #calculating the probability of masculine words in the masculine list
        
        p_masculine_list=[]
        for job_desc in masculine_freq:
            p_masculine={}
            for key,value in job_desc.items():
                if key=='<no words>':
                    p_masculine[key]=0
                else:
                    p_masculine[key]=value/len(masculine_coded_words)


            p_masculine_list.append(p_masculine)
            
        print(f'masculine words probability:{p_masculine_list}')
        prob_masculine=[]
        for job_desc in p_masculine_list:
            p_masculine_job_desc=1
            for word,value in job_desc.items():
                p_masculine_job_desc*= value 
            prob_masculine.append(p_masculine_job_desc)        
        #print(prob_masculine)       

        
    
        #### TASK C: For each word in the job_desc_words, check if they are in masculine_coded_list 
            #### multiply p_masculine_given_job_desc by 0.9 if keyword matches
        p_masculine_given_job_desc_list=[]
        for prob in prob_masculine:
            p_masculine_given_job_desc = self.p_masculine
            if prob!=0:
                p_masculine_given_job_desc*=prob
                p_masculine_given_job_desc=p_masculine_given_job_desc*0.9
                p_masculine_given_job_desc_list.append(p_masculine_given_job_desc)
            else:
                p_masculine_given_job_desc_list.append(0)
        print(f'total probability for masculine:{p_masculine_given_job_desc_list}')
        
        #print(p_masculine_given_job_desc)

            # for ... in ...:
            #     if ... in self.masculine_coded_words:
            #         p_masculine_given_job_desc *= 0.9  # Adjusted probability for masculine word

        return p_masculine_given_job_desc_list

        ###########################################################################################

    
    def calculate_p_feminine_given_job_desc(self, job_desc_words):
        '''
        calculate the probability of being feminine given the job_desc
        '''
        p_feminine_given_job_desc = self.p_feminine
        #print(p_feminine_given_job_desc)
        #create a feminine list from the job descrpiton
        feminine=[]
        for words in job_desc_words:
            f=[]
            for word in words:
                if word in feminine_coded_words:
                    f.append(word)
            feminine.append(f)
        print(f'feminine words:{feminine}')

        # Counting word frequencied in feminine list
        feminine_freq=[]
        for words in feminine:
            feminine_word_count={}
            if len(words)==0:
                feminine_word_count["<no words>"] = 0
            for word in words:
                if word in feminine_word_count:
                    feminine_word_count[word] += 1
                else:
                    feminine_word_count[word] = 1
                
            feminine_freq.append(feminine_word_count)
        print(f'feminine words frequency:{feminine_freq}')
        
        #calculating the probability of feminine words in the feminine list
        p_feminine_list=[]
        for job_desc in feminine_freq:
            p_feminine={}
            for key,value in job_desc.items():
                if key=='<no words>':
                    p_feminine[key]=0
                else:
                    p_feminine[key]=value/len(feminine_coded_words)


            p_feminine_list.append(p_feminine)
            
        print(f'feminine words probability:{p_feminine_list}')
        prob_feminine=[]
        for job_desc in p_feminine_list:
            p_feminine_job_desc=1
            for word,value in job_desc.items():
                p_feminine_job_desc*= value 
            prob_feminine.append(p_feminine_job_desc)        
        #print(prob_feminine)


        #### TASK D: For each word in the job_desc_words, check if they are in feminine_coded_list 
        
        # Calculate probabilities: multiply p_masculine_given_job_desc by 0.9 if keyword matches and adjust accordingly
        # Hint: similar to calculate_p_masculine_given_job_desc
        p_feminine_given_job_desc_list=[]
        for prob in prob_feminine:
            p_masculine_given_job_desc = self.p_masculine
            if prob!=0:
                p_feminine_given_job_desc*=prob
                p_feminine_given_job_desc=p_feminine_given_job_desc*0.9
                p_feminine_given_job_desc_list.append(p_feminine_given_job_desc)
            else:
                p_feminine_given_job_desc_list.append(0)
        print(f'total probability for feminine:{p_feminine_given_job_desc_list}')
        ###########################################################################################

        return p_feminine_given_job_desc_list



if __name__ == "__main__":
    
    # import libraries
    import pandas as pd
    import numpy as np
    from collections import Counter
    import string

    # Load CSV
    data = pd.read_csv("data.csv")

    # prepare training data
    train_job_descs = list(data['job_description'])[:14]
    train_labels = list(data['label'])[:14]

    # prepare test data
    test_job_descs = list(data['job_description'])[1:4]
    test_labels = list(data['label'])[1:4]

    # Predefined lists of feminine and masculine words
    feminine_coded_words = [
        "agree","affectionate","child","cheer","collab","commit","communal",
        "compassion","connect","considerate","cooperat","co-operat","shine","core",
        "depend","emotional","empath","feel","flatterable","gentle",
        "honest","interpersonal","interdependen","interpersona","inter-personal",
        "inter-dependen","inter-persona","kind","kinship","loyal","modesty", "families",
        "nag","nurtur","responsibilities","pleasant","polite","quiet","respon","sensitiv",
        "submissive","support","sympath","tender","together","trust","understand",
        "warm","whin","enthusias","inclusive","yield","share","sharin","truly", "valued","understood"
    ]


    masculine_coded_words = [
        "active","adventurous","aggress","ambitio",
        "analy","assert","athlet","autonom","battle","boast","challeng",
        "champion","compet","confident","courag","decid","decision","decisive",
        "defend","determin","domina","dominant","driven","fearless","fight",
        "force","greedy","head-strong","headstrong","hierarch","hostil",
        "impulsive","independen","individual","intellect","lead","logic",
        "objective","opinion","outspoken","persist","principle","reckless",
        "self-confiden","self-relian","self-sufficien","selfconfiden",
        "selfrelian","selfsufficien","stubborn","superior","unreasonab"
    ]

    # Create and train the Bayesian job_desc filter
    bayesian_filter = BayesianGenderBias(feminine_coded_words, masculine_coded_words)
    bayesian_filter.train(train_job_descs, train_labels)

    # Make predictions
    predictions = []
    predictions = bayesian_filter.predict(test_job_descs)

    print("Actual:", test_labels)
    print("Predictions:", predictions)































































































