print("----PERSYARATAN BEASISWA----")

status=str(input("status="))
semester=int(input("semester="))

if (status == "aktif") or (status == "Aktif") or (status == "AKTIF"):

	if(semester >=2 and semester <=6):
		print("Anda boleh mengajukan beasiswa")

	else:
		print("Anda tidak memenuhi syarat mengajukan beasiswa")