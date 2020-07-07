# colourcat4000 - colour code your highlights

This code extracts highlights from your pdfs and posts them to elasticsearch. It is tailored to cyborgs who like to code their highlights by colour.

Works with python 2.7. Might work with newer versions too.

## What else?

It watches a folder for changes and keeps the elasticsearch index up to date.

From the extracted highlights, the code creates "copy-pastable" bits, which you can cite via pandoc-citeproc (if the names of your pdfs match your citekeys).

```
"digital humanities are involved in the displacement of politically progressive humanities scholarship and activism in favor of the manufacture of digital tools and archives;" [@adema_disrupting_2016: 9]"
```

Can be browsed and searched via elasticsearch or by opening the markdown files in notes/ (default), which are created for each pdf.

### Colour-coding

There are many ways of engaging with a text. One approach I have come to like is organized around colour coded highlighting, with each colour denoting a category:

- argument, yellow - bits pertaining to the general argument and flow of the text, claims made;
- quote, orange - highly memorable/quotable bits;
- data, green - hard, indisputable, facts or definitions;
- derived, cyan - new texts to check/out read;
- useful, magenta - bits closely aligned to current interests, the motivation behind reading the text, or just containing stuff to be tried;

- continued, blue-grey - a sub category containing a further elaboration of any of the main categories above.

All main categories are tied to specific types of action. You'll look for cyan highlights if you're looking for things to read, for orange ones if you're looking for things to cite, for yellow ones if you're looking to summarize a text etc.


## Installation

Install elasticsearch. On Linux distros:

```
sudo apt-get update && sudo apt-get install elasticsearch
```
[More info](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

You might need to enable and start the elasticsearch service.

```
sudo service elasticsearch enable
sudo service elasticsearch start
```

Install other dependencies:

```
sudo apt install python-poppler
pip install -r requirements.txt
```

Edit settings.py to set the folder containing your pdfs and adjust the colour coding to your needs.

To find out which colours (denoted in 16-bit RGB) your pdf contains run

```
gib_colours.py your.pdf
```

Run changes.py or deploy it as a service. To accomplish the latter edit colourcat.service. Enter the path to the folder where you placed this code. Make sure that changes.py is executable. Then:

```
sudo cp colourcat.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable colourcat.service
sudo systemctl start colourcat.service
```

Optional: Install [elasticsearch-head](https://github.com/mobz/elasticsearch-head) (or similar) for more convenient browsing and searching through your highlights.
