from flask import Flask,redirect, render_template,url_for,request
import requests
from bs4 import BeautifulSoup


app =Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/scrape',methods = ['GET','POST'])
def scrape(): 
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=").text  
    soup = BeautifulSoup(html_text,"html.parser")
    jobs= soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    companies = []
    requirements = []
    for job in jobs:
        company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
        skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
        companies.append(company_name)
        requirements.append(skills)
    return render_template("home.html", content=companies , skill = requirements)
    
    
    
if __name__ == '__main__':
    app.run(debug=True)



