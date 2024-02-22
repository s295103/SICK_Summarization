import json
import spacy

nlp = spacy.load('en_core_web_sm')
text = "Customer:\t@AirbnbHelp Thanks. Hope to get in touch soon"

doc = nlp(text)

pass