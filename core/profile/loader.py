#!/usr/bin/env python
import os
import json
import decoder #, compiler

def loadProfile():
    #if not os.path.isfile('profile.json'):
        #compiler()
    profile = open('core/profile/profile.json')
    data = json.load(profile, object_hook=decoder.decode)
    profile.close()
    return data
