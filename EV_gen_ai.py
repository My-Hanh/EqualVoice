#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:39:35 2024

@author: cwolf
"""

from openai import OpenAI

#import seaborn as sns
#import matplotlib.pyplot as plt
#import pandas as pd


##########################################################################
def ai_compares(text):
    message = '''My goal is to develop an educational tool for journalists to
    raise awareness about gender bias in their articles. The goal is to flag where
    there is possible gender bias in the text of their article and to give suggestions 
    for improvement to use more inclusive language. Here is a text from an article:

    {text}

    Please give me feedback on 
    1. where there is possible gender bias in this text, 
    2. why it is problematic and 
    3. provide suggestions for improvement.
    '''.format(text=text)
    
    messages = [
            {
                'role': 'system',
                'content': 'you are an editor.'
            },
            {
                'role': 'user',
                'content': message
            }
    ]
    
    #https://platform.openai.com/docs/api-reference/chat/create
    #temperature 0-2
    #   We generally recommend altering this or top_p but not both.
    #   higher temp, lower temp, like scaling a dist
    #   0 temp is no scaling, gives nearly same answer, 2 very random
    #top_p 0-1
    #   We generally recommend altering this or temperature but not both.
    #   outputs 40000 tokens, 0.9 gives top probabilty output, more deterministic
    
    kwargs = {'max_tokens': 2048,'temperature': 0.8}
    #kwargs = {'max_tokens': 2048, 'temperature': 0.5}
    #kwargs = {'max_tokens': 2048, 'temperature': 0.2}

    client = OpenAI(
        base_url="http://localhost:4891/v1",
        api_key="not needed for a local LLM"
    )
    model = "mistral-7b-instruct-v0.1.Q4_0"

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        n=1,
        **kwargs
    )
    out = response.choices[0].message.content
    
    print(out)
    
    #return response
##########################################################################

t1 = "The sports club of Chicago’s club owner reported that the female members were beautiful, and further asked if the blonde was single. He owns a club on Michigan and 4th st, and has long been a champion for open access to the gym.  "
t2 = "The CEO was asked when she planned on having children. "

if __name__ == '__main__':
    ai_compares(t1)