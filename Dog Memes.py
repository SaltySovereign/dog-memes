#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
#region imports
import random
import urllib.request
from time import sleep
import requests
import praw
from InstagramAPI import InstagramAPI
import os
import sys


#endregion

InstagramAPI = InstagramAPI("deakin232@gmail.com", "Itwbost5!")
InstagramAPI.login()  # login
while True:
    #region redditapi
    reddit = praw.Reddit(client_id='qRmTSny9llNyDg',
                     client_secret='DISVDwXNIxhf9Dfuy3Oy1qKrI_g',
                     user_agent='ripper')

    submission_chosen = []

    for submission in reddit.subreddit('dogmemes').hot(limit=40):
        submission_chosen.append([submission.url,submission.author.name])

    submission_chosen.pop(0)
    submission_chosen.pop(0)
    #endregion
    

    #region create url and check if posted
    
    while True:
        t = random.choice(submission_chosen)
        author = t[1]
        t = t[0]
        
        caption = 'Credit: u/'+author
        i=0
        while True:
            i+=1
            try:
                fh = open(str(sys.path[0])+'/posted images/'+str(i)+".jpg", 'r')
            except FileNotFoundError:
                break
            
        file_url = str(sys.path[0])+'/posted images/'+str(i)+".jpg"
        try:
            urllib.request.urlretrieve(t,file_url)
        except:
            print("Failed to download image.")
            break
            
        try:
            InstagramAPI.uploadPhoto(file_url, caption=caption)
            print("Image posted")
            sleep(3600)
            break
        except:
            print("Failed")
            submission_chosen.pop(submission_chosen.index([t,author]))
            os.remove(file_url)
            break
    #endregion


    
    
