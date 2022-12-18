class Dad:
    basketball =1
    

class Son(Dad):
    dance = 1
    basketball = 9

    def isdance(self):
        return f"Yeah bitch  i dance {self.dance} no of times"


class Grandson(Son):
    dance = 6
   

    def isdance(self):
        return f"Yeah bitch  i dance a lot {self.dance} no of times"


mahesh = Dad()
ramesh = Son()
suresh = Grandson()

print(suresh.isdance()) #overrides the next one once same method is written
print(suresh.basketball)  # first search for 1st upper class than to other
