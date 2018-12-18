import re
name = ''
namelist = []

print('TypeManager Beta1.0.68Pre')
def home():
    print('已进入主编辑模式.')
    inputs = str (input('键入代码...'))
    global name
    global editname
    if re.match('accession',inputs):
        name = str (inputs[10:])
        namelist.append(name)
        print('已创建一个名称为',name,'的子类.')
        print('正在编辑',name,'子类...')
        accessions()
    elif re.match('look',inputs):
        looks()
    elif re.match('edit',inputs):
        global editname
        editname = str (inputs[5:])
        if editname in namelist:
            print('进入对',editname,'子类的编辑.')
            editing()
        else:
            print('未创建',editname,'子类!')
            home()
    else:
        print('代码错误,请重新输入.')
        home()
def accessions():
    accinputs = ''
    global name
    while True:
        accinputs = str (input('键入代码...'))
        if re.match('rename',accinputs):
            renames = str (accinputs[7:])
            print('已成功将子类',name,'的名称更改为',renames,'.')
            namelist[-1] = renames
            name = renames
            continue
        elif re.match('back',accinputs):
            home()
        else:
            print('代码错误，请重新输入.')
            continue
def editing():
    global editname
    while True:
        editinput = str (input('键入代码...'))
        if re.match('rename',editinput):
            editrename = str (editinput[7:])
            print('已将',editname,'的名称修改为',editrename)
            namelist[editname] = editrename
            editname = editrename
            continue
        elif re.match('back',editinput):
            home()
def looks():
    global namelist
    print('---全部显示子类---')
    for s in namelist:
        print(s)
    print('------------------')
    if namelist == []:
        print('您没有创建子类.')
    home()
home()

        

        
