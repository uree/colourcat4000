# -*- coding: utf-8 -*-

import archieml
import json
from collections import OrderedDict
import requests
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from settings import *


index_line = '{ "index": {}}'

def process(infile):
    infile_minus = infile.split('/')[-1]

    with open(infile) as f:
        data = archieml.load(f)
        data2 = json.loads(json.dumps(data))

    return data2


def del_by_bibkey(es_index, bibkey):
    headers = {'Content-Type': 'application/json'}
    data = {'query': {'match' : {'bib' : bibkey}}}
    data = json.dumps(data)
    url = 'http://localhost:9200/'+es_index+'/_delete_by_query?conflicts=proceed'
    r = requests.post(url, data=data, headers=headers)
    print(r.json())


def post2es(jsondata):
    headers = {'Content-Type': 'application/json'}
    es = Elasticsearch([{'host':'localhost', 'port': 9200}])

    postdata = jsondata['text'][0]['Highlight']

    helpers.bulk(es, postdata, index=es_index, doc_type=es_type, request_timeout=200)


def eldelete_all(es_index):
    data = {'query': {'match_all': {}}}
    data = json.dumps(data)
    url = 'http://localhost:9200/'+es_index+'/_delete_by_query?conflicts=proceed'
    r = requests.post(url, data=data)
    print(r.json())
