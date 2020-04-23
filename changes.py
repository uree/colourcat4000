#!/usr/bin/python2

# -*- coding: utf-8 -*-

# watchdog
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileSystemEvent

# general
import pprint
import sys

# mine
from archie import *
from extract import *
from settings import *

pp = pprint.PrettyPrinter(indent=4)



class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.src_path.endswith('.pdf'):
            output_filename = hl2md(event.src_path, md_folder)
            print("changes, output filename")
            print(output_filename)
            got_json = process(output_filename)
            pp.pprint(got_json)
            bibkey = got_json['text'][0]['Highlight'][0]['bib']
            del_by_bibkey(es_index, bibkey)
            post2es(got_json)
        else:
            pass

    def on_created(self, event):
        if event.src_path.endswith('.pdf'):
            output_filename = hl2md(event.src_path, md_folder)
            print("changes, output filename")
            print(output_filename)
            got_json = process(output_filename)
            pp.pprint(got_json)
            post2es(got_json)
        else:
            pass

if __name__ == '__main__':
    print("---init main changes_2018---")
    args = text_folder

    observer = Observer()
    observer.schedule(MyHandler(), path=args if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    print("Watchdog watching ...")
