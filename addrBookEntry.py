#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AddrBookEntry(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print('Created instance for:',self.name)  # 测试init是否被调用了

	
class EmplAddrBookEntry(AddrBookEntry):
    'Empoyee Address Book Entry class'	
    def __init__(self,nm,ph,email):
        AddrBookEntry.__init__(self,nm,ph)
        self.email = email
        print('Created instance EmplAddrBookEntry.')
	
def test():
    one = AddrBookEntry('Peter',120)
    sub = EmplAddrBookEntry('John',110,'John@gmail.com')
#output:
#Created instance for: Peter
#Created instance for: John
#Created instance EmplAddrBookEntry.