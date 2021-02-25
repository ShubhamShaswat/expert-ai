from expertai.nlapi.cloud.client import ExpertAiClient
import os

os.environ["EAI_USERNAME"] = '' #YOUR EMAIL 
os.environ["EAI_PASSWORD"] = '' #YOUR PASSWORD for the NLAPI 


class ExpertAi(object):

    def __init__(self,language='en'):
        self.client = ExpertAiClient()
        self.language = language

    #method for sentiment analysis
    def sentiment_analysis(self,text):
        output = self.client.specific_resource_analysis(
            body={"document": {"text": text}},
            params={'language': self.language, 'resource': 'sentiment'
        })
        return output.sentiment.overall

    #method to get entities
    def get_tokens(self,text):
        output = self.client.specific_resource_analysis(
            body={"document": {"text": text}},
            params={'language': self.language, 'resource': 'entities'
            })

        return output.entities


