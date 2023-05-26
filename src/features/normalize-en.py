import requests

def normalize(text):
    '''
    Normalize en text
    '''
    dict = {
        "text": text,
    }

    response = requests.post("https://grammar-genius.p.rapidapi.com/dev/grammar/", data=dict)
    prin
    return response

if __name__=="__main__":
    print(normalize("My name are Haong"))