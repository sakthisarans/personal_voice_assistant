import re
import google.generativeai as palm
import json

try:
    palm.configure(api_key='AIzaSyDZ2vRDZ2PkX4EJ0EwXO1_gOzqZR1bI-7A')
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
except Exception as ex:
    print(ex)
def palm_interact(query):
    return palm.generate_text(
        model=model,
        prompt=query,
        temperature=0,
        max_output_tokens=800,
    )
def get_bard_message(query):
    completion = palm_interact(query)
    try:
        string=completion.result.replace(". ","\n")
        out=[re.sub(r"[^a-zA-Z0-9\.\,]+", ' ', k) for k in string.split("\n")]
    except Exception as ex:
        print(ex)
        out=completion.result
    return out

def funny_reply(query):
    context=f"you are a funny person who engages a persons in a funny way. now a person gives you a situvation and generate a funny tnteractive text message with a short sentence for the following text. the text is {query}"
    completion = palm_interact(context)
    try:
        string=completion.result.replace(". ","\n")
        out=[re.sub(r"[^a-zA-Z0-9\.\,]+", ' ', k) for k in string.split("\n")]
    except Exception as ex:
        print(ex)
        out=completion.result
    return out

def extract_feature(query):
    examplejson="{'feature':'<>','appname':'<>'}"
    context=f"you are a very good text analizer. now you are going to anazlize the match case from the given text compared with the list of activities and if the case is openapp then return the app name and give the respnce as a valid JSON formate from the given list if doesnt matches means leave it empty.examplejson:{examplejson} doesnt include any extras to the structure, activity:['openapp','moviebooking','birthdaywish']. the user inputed text is '{query}'"
    completion = palm_interact(context)
    print(completion)
    out=''
    try:
        test=completion.result.replace("'","\"")
        print(test)
        out=(json.loads(test))
    except Exception as e:
        print(e)
        try:
            test = completion.result.split('\n')
            test[0] = ""
            test[test.__len__() - 1] = ""
            test = ("".join(test))
            print(test)
            out= (json.loads(test.replace("'","\"")))
        except Exception as ex:
            print(ex)
            out= {"feature":"","appname":""}
    print(out)
    return out


def time_extract(query):
    examplejson='{"time":"","date":"yyyy-mm-dd"}'
    context=f"context:you are an excellent text analizer. now you have to extract the date and time format from the text and return the data in a json format {examplejson}.text:{query}"
    completion=(palm_interact(context))
    out=""
    try:
        test=completion.result.replace("'","\"")
        print(test)
        out=(json.loads(test))
    except Exception as e:
        print(e)
        try:
            test = completion.result.split('\n')
            test[0] = ""
            test[test.__len__() - 1] = ""
            test = ("".join(test))
            print(test)
            out= (json.loads(test.replace("'","\"")))
        except Exception as ex:
            print(ex)
            out= {"time":"","date":""}
    print(out)
    return out

# print("--")
print(extract_feature("dayaffter tomorrow is my friends birthday wish him a message in midnighr 12 o clock"))
