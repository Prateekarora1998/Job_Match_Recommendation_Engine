# -*- coding: utf-8 -*-
"""
@author: Prateek Arora
"""

from recommendationEngine import jobRecommendationEngine
import pytest
import pandas as pd

def test_read_csv_files_exception(): 
    with pytest.raises(FileNotFoundError):
        jobRecommendationEngine.readCSVFiles('jobfile.csv')
        
def test_read_csv_files():
    assert jobRecommendationEngine.readCSVFiles('jobs.csv').empty == False
    
def test_jobseeker_jobs():
    
   jobsDataFrame = pd.DataFrame([[1,'Python Developer', 'Python, SQL, Flask, Django'], [2, 'Frontend Developer', 'Angular, React.js, HTML']], columns = ['id', 'title', 'required_skills'])
   jobseekerDataFrame = pd.DataFrame([[1,'Alice', 'Python, SQL, Django'], [2, 'Peter', 'Angular, React.js, Flask, HTML']], columns = ['id', 'name', 'skills'])
   finalDataFrame = pd.DataFrame([[1,'Alice', 1, 'Python Developer', 3, 75.0], [1,'Alice', 2, 'Frontend Developer', 0, 0.0], [2,'Peter', 2, 'Frontend Developer', 3, 100.0], [2, 'Peter', 1, 'Python Developer', 1, 25.0]], columns = ['Jobseeker_ID', 'Jobseeker_Name', 'Job_ID', 'Job_Title', 'Matching_Skill_Set', 'Matching_Skill_Percentage'])
   outputDataFrame = jobRecommendationEngine.calculatePercentage(jobsDataFrame, jobseekerDataFrame)
   
   assert finalDataFrame.equals(outputDataFrame) == True
   
def test_division_by_zero():
    
    with pytest.raises(ZeroDivisionError):
        jobsDataFrame = pd.DataFrame([[1,'Python Developer', 'Python, SQL, Flask, Django'], [2, 'Frontend Developer', '']], columns = ['id', 'title', 'required_skills'])
        jobseekerDataFrame = pd.DataFrame([[1,'Alice', 'Python, SQL, Django'], [2, 'Peter', 'Angular, React.js, Flask, HTML']], columns = ['id', 'name', 'skills'])
        jobRecommendationEngine.calculatePercentage(jobsDataFrame, jobseekerDataFrame)
    
def test_lowercase_uppercase_skills():
    
    jobsDataFrame = pd.DataFrame([[1,'Python Developer', 'PYTHON, SQL, FLASK, django'], [2, 'Frontend Developer', 'ANGULAR, React.js, html']], columns = ['id', 'title', 'required_skills'])
    jobseekerDataFrame = pd.DataFrame([[1,'Alice', 'Python, SQL, Django'], [2, 'Peter', 'angular, React.js, Flask, HTML']], columns = ['id', 'name', 'skills'])
    finalDataFrame = pd.DataFrame([[1,'Alice', 1, 'Python Developer', 3, 75.0], [1,'Alice', 2, 'Frontend Developer', 0, 0.0], [2,'Peter', 2, 'Frontend Developer', 3, 100.0], [2, 'Peter', 1, 'Python Developer', 1, 25.0]], columns = ['Jobseeker_ID', 'Jobseeker_Name', 'Job_ID', 'Job_Title', 'Matching_Skill_Set', 'Matching_Skill_Percentage'])
    outputDataFrame = jobRecommendationEngine.calculatePercentage(jobsDataFrame, jobseekerDataFrame)

    assert finalDataFrame.equals(outputDataFrame) == True
