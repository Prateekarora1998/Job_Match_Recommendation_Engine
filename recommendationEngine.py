# -*- coding: utf-8 -*-
"""
@author: Prateek Arora
"""

import pandas as pd
from operator import itemgetter

class jobRecommendationEngine:
    
    def readCSVFiles(csvFile):
        try:
            data = pd.read_csv(csvFile)
        except:
            raise FileNotFoundError
        return data
    
    def calculatePercentage(jobsDataFrame, jobseekerDataFrame):
        
        combinedData= []
        try:
            for i in jobseekerDataFrame.index:
                combineNewData = []
                for j in jobsDataFrame.index:
                    
                    ## Change the skills to lowercase
                    jobseekerSkills = [x.lower() for x in list(jobseekerDataFrame['skills'][i].split(', '))]
                    jobsSkills = [x.lower() for x in list(jobsDataFrame['required_skills'][j].split(', '))]
                
                    matchingSkillCount = len(set(jobseekerSkills) & set(jobsSkills))
                    count = 0 if jobsSkills == [''] else len(jobsSkills)
                    matchingSkillPercentage =  (matchingSkillCount/count)*100                
                    ## Create a new list of datas to append to a new lists
                    newData = [jobseekerDataFrame['id'][i], jobseekerDataFrame['name'][i], jobsDataFrame['id'][j], jobsDataFrame['title'][j], matchingSkillCount, matchingSkillPercentage]
                    combineNewData.append(newData)
                
                ## Sort the list by Matching Skill Percentage
                combinedData.extend(sorted(combineNewData, key=itemgetter(5), reverse=True))
            
                ## Sort the list by Job ID if Matching Skill Percentage are same 
                for i in range(len(combinedData)-1):
                    if ((combinedData[i][2] > combinedData[i+1][2]) and (combinedData[i][5] == combinedData[i+1][5])):
                        combinedData[i], combinedData[i+1] = combinedData[i+1], combinedData[i]
         
            newDataFrame = pd.DataFrame(combinedData, columns = ['Jobseeker_ID', 'Jobseeker_Name', 'Job_ID', 'Job_Title', 'Matching_Skill_Set', 'Matching_Skill_Percentage']) 
            
            return newDataFrame
        
        except ZeroDivisionError:
            raise ZeroDivisionError
            print("There are no skills present in job's skills section to match. Please check")
            
        except Exception as e:
            print(e)
        
jobs = jobRecommendationEngine.readCSVFiles('jobs.csv')
jobseeker = jobRecommendationEngine.readCSVFiles('jobseekers.csv')
result = jobRecommendationEngine.calculatePercentage(jobs, jobseeker)
print(result)