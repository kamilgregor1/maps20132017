# -*- coding: utf-8 -*-
# python 3
import csv
import json
from slugify import slugify

party = 'kscm'
percent = 10

i = 0
people = []
votes = []
winners = {}
with open('obce_geocoded_adj.csv','r') as f:
  csvreader = csv.reader(f,delimiter=",")
  for row in csvreader:
    if i <= 1:
      if i == 1:
        for j in range(10,49):
          people.append(row[j])
          winners[row[j]] = 0
    else:
      r = {}
      r['id'] = row[4]
      r['town'] = row[5]
      r['lat'] = row[50]
      r['lng'] = row[49]
      r['votes'] = []
      maxi = 0
      sumi = 0
      for j in range(0,38):
        if slugify(people[j]) == party:
          r['votes'].append(int(row[j+10]))
      r['votes'].append(int(percent/100*int(row[9])))
        
#        r['votes'].append(row[j+10])
#        sumi = sumi + int(row[j+10])
#        if (int(row[j+10])) > maxi:
#          winner = people[j]
#          maxi = int(row[j+10])
#      r['winner'] = winner
#      r['winner_class'] = slugify(winner),
#      r['population'] = sumi
#      winners[winner] = winners[winner] + 1  
      votes.append(r)

    i = i + 1
      
#print(winners)
 
#print(people)
#print(r)
#raise(Exception,'dipy')  

colors = {
  'ne-brusel': '#888',
  'moravane': '#888',
  'top-09': '#808',
  'aneo': '#888',
  'snk-ed': '#888',
  'svobodni': '#080',
  'lev-21': '#888',
  'hss': '#888',
  'pirati': '#000',
  'vize-2014': '#888',
  'kdu-csl': '#fedc35',
  'cssd': '#f54200',
  'kscm': '#ff0000',
  'rds': '#888',
  'vv': '#888',
  'ksc': '#888',
  'zeleni': '#0b0',
  'antibursik': '#888',
  'les': '#888',
  'usvit': '#0ff',
  'rozumni': '#888',
  'ods': '#008',
  'sp-a-no': '#888',
  'ano': '#009ee0'
}

#data = {'people':people,'votes':votes,'colors':colors}
with open('epcz_'+party+'_'+str(percent)+'_2014.json', 'w') as outfile:
  json.dump(votes, outfile)
outfile.close()
