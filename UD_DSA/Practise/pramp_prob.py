class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        rep1 = IP.split(":")
        rep2 = IP.split(".")
        # print(rep1,rep2)
        if (len(rep1) == 1 and len(rep2) == 1):
            return "Neither"
        
        #Tells this is Ipv4
        if len(rep1) == 1:
            # pritn("hi")
            if len(rep2) != 4:
                return "Neither"
            #Write logic
            for i in rep2:
                try:
                    if int(i) > 255 or (len(i) >1 and int(i[0]) == 0):
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"
            
        
        #Tells this is Ipv6
        if len(rep2) == 1:
            # print("holla")
            #Write logic
            if len(rep1) != 8:
                return "Neither"
            for i in rep1:
                if(len(i) > 4 or (not i.isalnum())):
                    return "Neither"
                for char in i:
                    if char.lower() >= 'g':
                        return "Neither"
            return "IPv6"