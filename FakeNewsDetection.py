import nltk
import nltk.data
from nltk import word_tokenize, pos_tag, ne_chunk
import os
import os.path
import urllib2
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import re

headline=raw_input("Enter the news headline: ")
terms=['Avalanches','Landslides','Earthquakes','Sinkholes','Volcanic eruptions','Volcanos','Floods','Limnic eruptions','Tsunami','Blizzards','Cyclones','Droughts','Cyclonic storms','Thunderstorms','Hailstorms','Heat waves','Tornadoes','Wildfires','Airburst','Solar flare','Hurricanes']
flag=0
tokenized = nltk.word_tokenize(headline)
tagged = nltk.pos_tag(tokenized)
#print tagged
namedEnt = nltk.ne_chunk(tagged)
#namedEnt.draw()
'''for chunk in namedEnt:
	if hasattr(chunk,'label'):
		print(chunk.label(),''.join(c[0] for c in chunk))'''
				
for chunk in namedEnt:
	for c in chunk:
		if hasattr(chunk,'label'):
			for term in terms:
				p=fuzz.partial_ratio(c[0],term)
				#print p,
				if(p>=90):
					flag=1
					print "Matched with valid entity"
	
			#print(process.extract(c[0],terms))
			#print "One chunk done",''.join(c[0])
if flag==1:
	print "Format matched.\nValidating the news..."
else:
	print "Format does not match.\nHowever, checking for its occurence..."

page = urllib2.urlopen("https://www.usgs.gov/news/news-releases").read()
f=open("news.txt","w")
f.write(str(page))
f.close()

page = urllib2.urlopen("https://www.livescience.com/topics/natural-disasters").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("https://www.theguardian.com/world/natural-disasters").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("https://www.scientificamerican.com/natural-disasters/").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("https://www.ndtv.com/topic/natural-disaster").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("http://www.downtoearth.org.in/natural-disasters").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("http://www.foxnews.com/category/science/planet-earth/natural-disasters.html").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("http://www.gdacs.org/default.aspx").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("https://www.firstpost.com/tag/natural-disaster").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("http://www.newsnow.co.uk/h/Current+Affairs/Natural+Disasters").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

page = urllib2.urlopen("https://www.bbc.com/news/world").read()
f=open("news.txt","a")
f.write(str(page))
f.close()

f=open("headlines.txt","w")
f.write(str(os.system("html2text news.txt > headlines.txt")))
f.close()

term = headline
term1=term.split()
term1=[x.lower() for x in term1]
#print term1
file = open('headlines.txt')
#stop_words = set(stopwords.words('english'))
stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn','killed','died','missing','panic','emergency','disturbance','tragedy','death-toll','casualties','loss','fatality','victims']

def common_member(a, b):
     
    a_set = set(a)
    b_set = set(b)
     
    # check length/size of intersection of two sets 
    if len(a_set.intersection(b_set)) == 2:
	return 1  
    else:
        return 0

for line in file:
    cnt=0
    line.strip().split('/n')
    line1=re.split(':|\s',line)
    filtered_sent = [w for w in line1 if not w in stop_words] 
    filtered_sent = [x.lower() for x in filtered_sent]
	
    p=common_member(term1,filtered_sent)
	
    if (p==1):	
	f=open("related.txt","a")
	f.write(line)
        f.close()
file.close()


filename = "related.txt"
if(os.path.isfile(filename)):
    with open("related.txt") as f:
        with open("relatednews.txt", "w") as f1:
            for l in f:
                f1.write(l)
    print "Valid News"
    os.remove("related.txt")

else:
    print "Fake News."



