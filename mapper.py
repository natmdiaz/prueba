#!/usr/bin/env python
import operator
import sys	

j=1
#ocupaciones_file = open ("a.txt",'r').readlines ()
diccionario = open("ejemplito2.txt",'r').readlines()
#corregido = open ("corregido.txt", 'w')
for line in sys.stdin:
	oc=line.rstrip().split(' ')
	word_x= (len(oc))
	i=0
#	diccionario = open("ejemplito2.txt",'r').readlines()
	for li in diccionario:
		x = li.rstrip().split('\t')
		word_dicc = (len(x))
		j=1
		i=0
		while (i<word_x):
			j=1
			while (j<word_dicc):
				#print ("gola")
				#print (oc[i], x[j])
				if(oc[i]==x[j]):
					oc[i]=x[0]
					#print (oc)
					#print (oc[i])
				j=j+1
			i=i+1
	palabra= ' '.join(oc)
	corregido.write('\n')
	corregido.write(palabra)
	#corregido.write('\n')
	print  '%s \ t %s' % ( palabra ,  1 )
	#print (palabra)
	#diccionario.close()

#    for li in diccionario:
 #       x = li.rstrip().split('\t')
