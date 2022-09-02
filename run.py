#!/usr/bin/env python3



#=============== YouTube search ================#
# By SlavPH : https://github.com/SlavPH

# This plugin is used to search on Youtube
# by the given text
# You can use this tool in Telegram bots!

# You must get your X-RapidAPI-Key from here:
# https://rapidapi.com by signing up!

# This API is free with unlimited requests
# and the rate limit is "30 requests per minute"
# You need to subscribe to this API in "Pricing"
# section and get your token from "Endpoints" section


import requests
import time
import json
import sys


#==================# Config #===================#
API_Key = "Your X-RapidAPI-Key here"

reset = "\033[m"      # reset
red   = "\033[1;91m"  # red
white = "\033[1;97m"  # white


#==========# YouTube search function #==========#
def YTsearch(string):
    global API_Key

    url = "https://simple-youtube-search.p.rapidapi.com/search"

    querystring = {"query":string,"safesearch":"false"}

    headers = {
        "X-RapidAPI-Key": API_Key,
        "X-RapidAPI-Host": "simple-youtube-search.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    
    Result = []
    for i ,item in enumerate(result["results"]):
        results = result["results"][i]
        uploadedAt = results["uploadedAt"]
        thumbnail = results["thumbnail"]
        url = thumbnail["url"]
        VId = results["id"]
        views = results["views"]
        Type = results["type"]
        live = results["live"]
        title = results["title"]
        private = results["private"]
        url = results["url"]
        duration = results["duration"]
        duration_formatted = results["duration_formatted"]
        channel = results["channel"]
        name = channel["name"]
        CId = channel["id"]
        
        # I used some of this information in result
        # You can use more! like "Type", "views"

        Result.append(f"""======================================
〔⚜️ {i+1}〕 ⏱ {uploadedAt}
👤 ᴄʜᴀɴɴᴇʟ: {name}
💭 ᴛɪᴛʟᴇ: {title}

🖇 {url}


""")
        Length = str(len(Result))
        
    return [Result, Length]


#=================# Ascii art #=================#
art = f"""
{red}                                            ,----,                                
{red}                                          ,/   .`|                                
{red}                                        ,`   .'  :                                
{red}        ,---,{white}                    {red}     ;    ;     /{white}             ,---,              
{red}       /_ ./|{white}   ,---.           ,--,{red}.'___,/    ,'{white}        ,--,,---.'|              
{red} ,---, |  ' :{white}  '   ,'\        ,'_ /|{red}|    :     |{white}       ,'_ /||   | :              
{red}/___/ \.  : |{white} /   /   |  .--. |  | :{red};    |.';  ;{white}  .--. |  | ::   : :      ,---.   
{red} .  \  \ ,' '{white}.   ; ,. :,'_ /| :  . |{red}`----'  |  |{white},'_ /| :  . |:     |,-.  /     \  
{red}  \  ;  `  ,'{white}'   | |: :|  ' | |  . .{red}    '   :  ;{white}|  ' | |  . .|   : '  | /    /  | 
{red}   \  \    ' {white}'   | .; :|  | ' |  | |{red}    |   |  '{white}|  | ' |  | ||   |  / :.    ' / | 
{red}    '  \   | {white}|   :    |:  | : ;  ; |{red}    '   :  |{white}:  | : ;  ; |'   : |: |'   ;   /| 
{red}     \  ;  ; {white} \   \  / '  :  `--'   \\{red}   ;   |.'{white} '  :  `--'   \   | '/ :'   |  / | 
{red}      :  \  \\{white}  `----'  :  ,      .-./{red}   '---' {white}  :  ,      .-./   :    ||   :    | 
{red}       \  ' ;{white}          `--`----'                {white}`--`----'   /    \  /  \   \  /  
{red}        `--` {white}   https://github.com/SlavPH                   `-'----'    `----'   
                                                                                 
"""


#====================# Main #====================#
def main():
    global art, red, reset, white

    print(art)

    text = "What do you like to search?\n"
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

    user_input = input(f"{red}>>>{reset} ")
    text2 = f"\n{white}Searching! Please wait...{reset}\n"
    for i in text2:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

    output = YTsearch(user_input)
    length = output[1]
    result = output[0]

    print(f"{red}{length}{white} results found!{reset}\n")
    for item in result:
        print(item)


# Comment this section if you want to use this tool 
# as plugin in other tools and just write "main()"

if __name__ == "__main__":
    main()