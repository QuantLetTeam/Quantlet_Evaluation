# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:02:37 2018
"""

import os
# Change working directory to the repository path
os.chdir('../Quantlet_Evaluation')

# Loading QUANTLET class
from modules.QUANTLET import QUANTLET

# Add github token, if you try to access a private repository or 
# to have a higher access limit.
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
