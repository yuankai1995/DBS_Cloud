#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# ### request is to get things from internet.... post is you give

# In[2]:


app = Flask(__name__)  


# ## Decorator, you need to run the thingy before the program

# In[3]:


import joblib

@app.route("/", methods = ["GET", "POST"])   # whenever we have multiple items in an array we need to use a square bracket
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return (render_template("index.html", result1=r1, result2=r2))
    else:                                     # before you press enter, it will come here
        return (render_template("index.html", result1="waiting", result2="waiting"))


# In[ ]:


if __name__ == "__main__":                   # if this program is yours, then run, else dont run
    app.run()
                                             # WSGI is what python uses to talk to frontend and backend   


# ## development environment.
# for cloud to use python, you need to use gunicorn.
# Gunicorn is a software.
# What protocol are you using? WSGI as our protocol.
# What are the things you want to upload the container?..
# Hyper parameter
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




