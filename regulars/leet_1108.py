def defangIPaddr(address):
	return address.replace(".","[.]")
address = "1.1.1.1"
print(defangIPaddr(address))
    