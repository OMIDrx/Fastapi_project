from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

mylist = [10,20,30,40]


@app.get('/home')
def home():
    return{'HELLO':'OMID'}


@app.get('/getItem/')
def get_all_Items():
    return {'mylist':mylist}

@app.post('/item/{new_item}')
def add_item(new_item : int):
    mylist.append(new_item)
    return {'mylist': mylist}

@app.get('/get_item/{index}')
def get_item(index : int):
    if index >= len(mylist):
        return 'index Not Found'
    else:
        return{f'your item:{mylist[index]}'}
    
@app.get('/lastItem')
def get_lastItem():  
    if mylist :
        return mylist[-1]
    else:
        return 'ERORRRRRRRRR'
'''   
@app.get('/lastItem')
def get_lastItem(): 
    if len(mylist) > 0 :
        return {f'last item':{mylist[-1]}}
    else:
        return 'erorr'
    
'''

@app.put('/update_item/{new_item}')
def update_item (new_item:int,old_item:int):
    index = 0
    if old_item in mylist:
        index = mylist.index(old_item)
        mylist[index] = new_item
        return {'new my list': mylist}
    else:
        return {'Item not Found'}
    
@app.put('/update_item_byindex/')
def update_item_byindex (index:int,new_number:int):
    if index < len(mylist):
        mylist[index] = new_number
        return {'new my list': mylist}
    else:
        return {'index not found'}

    
@app.delete('/delete_index/')
def delete_index(index:int):
    if index < len(mylist):
        result = mylist.pop(index)
        return {f'{result} delete from list '}
    else:
        return {' index not Found'}
    
@app.delete('/delete_item/')
def delete_item(item:int):
    if item not in mylist:
        return 'item not in my list'
    else:
        result = mylist.remove(item)
        return {f'{result} delete from list '}

@app.get('/reverse_list')
def reverse_list():
    if mylist :
            return mylist[::-1]
    else:
        return 'ERORRRRRRRRR'

