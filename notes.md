## Stuff to still SINK IN

1. MARKDOWN Tips: 
- use backlash \\ to include underscores \_ in the markdown code format

2. Testing SETUP: 
- have the run_tests.py in the main project folder
- - have it import unitest, the classes/models with the file path
- - and the: 
<code><p> if \_\_name\_\_ == '\_\_main\_\_': <br> unittest.main() </p></code>
- - within each 
- class NameConvention(unittest.TestCase):
- def setUp(self):
- def test_the_name_of_test(seld):
- expected(to fail),expected(to pass), actual, self.assertEqual(expected,actual)

3. Repositories and CRUD:
- import run_sql from the relevant dir and the class from the location
- create CRUD functions initiating them with the sql = "", values = [ This is a list] ,results = sql(sql,values)

CREATE
READ
UPDATE
DELETE

#SAVE
#SELECT ALL
#SELECT one using ID
#DELETE ALL
#DELETE one using ID
#UPDATE one using ID


FOR SELECT(ID)!!!: 
MAKE SURE to add * in the SELECT syntax!!! 


4. CONTROLLERS AND HTML
use default 'html5' to autopopulate your base.html
use {%block block_name1%}    the content from another file   {%endblock%} to indicate where you will have the content form another file
use {% extends 'filename.html%} with {%block block_name1%} put stuff here {%blockend%}

CSS IS EVIL

you cannot place a block in another block
also cannot have 2 blocks next to each other 
{%block foo%} {%endblock%}
{%block foo%} {%endblock%}  will give error for calling same block more than once

{%block foo1%} {%endblock%}
{%block foo2%} {%endblock%}




ADDING BASKET: 

in stock.py - added basket variable to stock class
Inventory.psql - added basket to TABLE
stock repository - added basket variable throughtout the methods


FLASK - when you accidentally stop the process using CTRL+Z, resume by putting 'fg %1' in console
