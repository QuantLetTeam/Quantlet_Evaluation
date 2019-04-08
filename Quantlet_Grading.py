# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:02:37 2018
"""
import os
os.chdir('/home/ms/github/quantlet_grading_one')

from modules.QUANTLET import QUANTLET
github_token = None
USER = 'quantlet'
repo = 'VIX'

q = QUANTLET(github_token=github_token, user=USER)
q.download_metafiles_from_user([repo])

q.grading().to_csv('grades_%s_%s.csv'%(USER,repo))
