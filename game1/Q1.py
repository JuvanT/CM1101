Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> room_reception = {}
>>> room_reception["south"] = "Admins"
>>> room_reception["east"] = "Tutor"
>>> room_reception["west"] = "Parking"
>>> room_recpetion
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    room_recpetion
NameError: name 'room_recpetion' is not defined
>>> room_reception
{'south': 'Admins', 'east': 'Tutor', 'west': 'Parking'}
>>> room_admins = {}
>>> room_admins["north"] = "Reception"
>>> 
>>> room_admins
{'north': 'Reception'}
>>> room_tutor = {}
>>> room_tutor["west"] = "Reception"
>>> room_tutor
{'west': 'Reception'}
>>> room_parking = {}
>>> room_parking["south"] = "Reception"
>>> room_parking["east"] = "Office"
>>> room_parking
{'south': 'Reception', 'east': 'Office'}
>>> room_office = {}
>>> room_office = ["west"] = "Parking"
SyntaxError: can't assign to literal
>>> room_office["west"] = "Parking"
>>> room_office
{'west': 'Parking'}
>>> 
