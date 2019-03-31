import billboard
import json
import datetime
 
 
outfilename = 'output.psv'
counter = 1000
chart_type = 'hot-100'
chart = billboard.ChartData(chart_type)
chart_date = '2017-07-01'
first_line = 'date | title | artist | weeks | delta | current | peak | previous | spotifyID\n'
 
 
with open(outfilename, 'a') as outputfile:
   outputfile.write(first_line)
 
 
for i in range (1,counter+1):
    for position in range (0,99):
        song = chart[position]
        line_out = unicode(str(chart_date) + ' | ' + unicode(song.title) + ' | ' + unicode(song.artist) + ' | ' + str(song.weeks) + ' | ' + str(song.change) + ' | ' + str(position) + ' | ' + str(song.peakPos) + ' | ' + str(song.lastPos) + ' | ' + str(song.spotifyID) + '\n')
        songidout = str(song.spotifyID) + '\n'
        with open(outfilename, 'a') as outputfile:
            outputfile.write(line_out.encode('utf8'))
    print chart.previousDate
    print chart[0]
    chart_date = chart.previousDate
    chart = billboard.ChartData(chart_type, str(chart.previousDate))
print 'done'
