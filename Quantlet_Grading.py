# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:02:37 2018
"""

import os
# Change working directory to the repository path
os.chdir('/home/ms/github/quantlet_evaluation')

# Loading QUANTLET class
from modules.QUANTLET import QUANTLET

# Add github token, if you try to acces a private repository or there are a lot of files to be checked
github_token = None
# set the user name 
USER = 'quantlet'
# set name of repository
repo = 'VIX'

# Quantlets are downloaded
q = QUANTLET(github_token=github_token, user=USER)
q.download_metafiles_from_user([repo])

# Quantlets are graded.
q.grading().to_csv('grades_%s_%s.csv'%(USER,repo))
