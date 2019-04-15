import csv

siswa = [
    ('Abdul','RPL X-4','90'),
	('Budi','RPL X-2','98'),
	('Chandra','RPL X-1','88'),
	('Denis','RPL X-3','78'),
	('Erlan','RPL X-1','89'),
	('Ferdi','RPL X-2','90'),
	('Ghina','RPL X-3','88'),
	('Hendri','RPL X-4','87'),
	('Indah','RPL X-1','80'),
]


f = open('siswa.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama','Kelas','Nilai'))


for s in siswa:
    w.writerow(s)

f.close()