class test:
    def __init__(self):
        self.value = 10
        self.name = 'wyw'
        self.psw = '54123697'
obj = test.__dict__

# for key, value in obj.items():
#     print(key,value)
obj = test()

attributes = test.__dict__
for attr_name, attr_value in attributes.items():
    print(getattr(obj,attr_name))