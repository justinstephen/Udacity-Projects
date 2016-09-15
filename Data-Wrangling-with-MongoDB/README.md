## Problems	encountered	in	your	map
The	first	thing	I	explored	in	the	data	downloaded	was	any	potential	problems	found	in	the	dataset.	During	my	initial	audit	of the	dataset,	I	found	the	following	issues:
* Inconsistent	street	names:	Different	abbreviations,	and	different	formatting	meant	that	many	streets	that	should	be	the	same i.e.:	Street,	St,	St.	were	all	being	categorized	separately.	
* Inconsistent	Zip	Codes:	Most	zip	codes	were	consistent	but	there	were	some that	were	just	marked	as	“Disneyland”,	some	that began	with	the	CA- prefix,	and	some	that	had	the	4-digit	extension	at	the	end.

To	address	the	street	issue,	I	first	put	together	a	mapping	of	the	abbreviations	that	would	need	to	be	updated,	and	what	they	should	be	updated	to:

``` python
mapping	=	{	"St":	"Street",
												"St.":	"Street",
												"Rd."	:	"Road",
												"Ave"	:	"Avenue",
												"Dr"	:	"Drive",
												"Dr."	:	"Drive",
												"Pkwy"	:	"Parkway",
												"Pkwy."	:	"Parkway",
												"Rd"	:	"Road",
												"Av"	: "Avenue",
												"Ave."	:	"Avenue",
												"Blvd"	:	"Boulevard",
												"Blvd."	:	"Boulevard",
												"Ln."	:	"Lane",
												"WAY"	:	"Way"
												}
```

Once	I	had	created	this	dictionary	of	mappings,	I	used	a	function	to	update	the	street names	to	their	non-abbreviated	versions.

I	noticed	the	zip	code	issue	after	I	had	imported	the	data	into	MongoDB	and	run	some	initial	queries.	To	address	this	issue,	I	created	a	function	that	would	strip	the	“CA”	off	of	the	beginning	of	any	zip	codes, or	strip	off	any	trailing	4-digit	extensions.

## Overview of the data:
#### File Size:
| File | Size |
| :--- | ---: |
|orangecounty.osm | 197.80MB|
|orangecounty.osm.json | 212.60MB|

#### How many unique users?
``` python
len(db.distinct("created.user"))
869
```
#### How many nodes?
``` python
db.find({"type":"node"}).count()
795519
```
#### How many ways?
``` python
db.find({"type":"way"}).count()
108177
```
#### Querying Zip Codes:
``` python
pprint.pprint(list(db.aggregate([{"$match":{"address.postcode":{"$exists":1}}},\
                                 {"$group":{"_id":"$address.postcode",	
                                            "count":{"$sum":1}}},\
                                 {"$sort":{"count":-1}}])))
```
#### Top 10 Amenities:
``` python
pprint.pprint(list(db.aggregate([{"$match":{"amenity":{"$exists":1}}},\
                                 {"$group":{"_id":"$amenity","count":{"$sum":1}}},\
                                 {"$sort":{"count":-1}},\
                                 {"$limit":10}])))
```
``` python
[  
   {  
      u'_id':u'parking',
      u'count':1061
   },
   {  
      u'_id':u'school',
      u'count':640
   },
   {  
      u'_id':u'restaurant',
      u'count':522
   },
   {  
      u'_id':u'fountain',
      u'count':410
   },
   {  
      u'_id':u'fast_food',
      u'count':361
   },
   {  
      u'_id':u'bench',
      u'count':289
   },
   {  
      u'_id':u'place_of_worship',
      u'count':275
   },
   {  
      u'_id':u'toilets',
      u'count':271
   },
   {  
      u'_id':u'fuel',
      u'count':189
   },
   {  
      u'_id':u'drinking_water',
      u'count':188
   }
]
```

## Other	ideas	about	the	dataset:
As populated	as	this	area	is,	it	looks	like	the	data	is	not	very	clean,	and	is	still	missing	a	lot	of	data.	While	doing	queries	on	the	different	tags	I	noticed	many	“yes”	entries,	which	indicated	that	there	was	not	a	more	specific	tag	applied.	One	interesting	project	that	I	could	see	this	data	being	used	for	is	combining	it	with	census	population	data	for	a	certain	zip	codes	or	cities.	You	could	compare	the	population	and	size	of	certain	areas	(zip	codes	or	cities)	and	compare	it	to	the	amount	of	city	provided	amenities	(parks,	fire	departments,	walkways,	etc.)	to	ensure	that	each	population	and	area	was	provided	enough	amenities.	You	could	probably	look	at	the	average	amount	of	amenities	for	population,	and	then	get	a	good	idea	of	if	it’s	enough	by	comparing	each	area	to	the	average,	and	seeing	if	it	is	above	or	below.	Another	interesting	idea	would	be	to	add	an	additional	tag	to	the	“sport”	tag	to	indicate	if	the	area	was	free	/	public	to	use	or	if	it	was	a	private	facility	that	you	must	pay.	This	would	create	an	interesting	way	to	search	the	map	and	you	wanted	to	see	where	you	could	go	to	play	that	sport.	This	would	require	significant	user	contribution	and	would	probably	have	to	be	updated	frequently	as	business	came	and	went	out	of	business.	Because	the	granular	data	in	the	map	is	already	so	sparse,	this	seems	like	it	would	probably	not	be	very	successful.	
