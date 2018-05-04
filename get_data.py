import io

from statistics import mean

# TOP FILE
top_cpu_list = list()
top_mem_list = list()
top_shr_list = list()
top_res_list = list()
top_ni_list = list()
top_virt_list = list()
c1 = 0

file = open("top.txt", "r") 

for line in file: 
	c1 += 1
	line_arr = line.split()
	
	#line_arr[0] # pid
	#line_arr[1] # name
	#line_arr[2] # PR
	
	top_ni_list.append(float(line_arr[3])) # NI
	top_virt_list.append(float(line_arr[4])) # VIRT
	top_res_list.append(float(line_arr[5])) # RES
	top_shr_list.append(float(line_arr[6])) # SHR
	#line_arr[7] # S

	top_cpu_list.append(float(line_arr[8].replace(",","."))) # CPU
	top_mem_list.append(float(line_arr[9].replace(",","."))) # MEM

file.close()
print()
print("TOP amount : " + str(c1))
print("NI : " +  str(mean(top_ni_list)))
print("VIRT : " +  str(mean(top_virt_list)))
print("RES : " +  str(mean(top_res_list)))
print("SHR : " +  str(mean(top_shr_list)))
print("CPU : " +  str(mean(top_cpu_list)))
print("MEM : " +  str(mean(top_mem_list)))	



# get dstat values

dstat_idl = list()
dstat_sys = list()
dstat_usr = list()
dstat_sig = list()
dstat_used = list()
dstat_free = list()
dstat_buff = list()
dstat_cach = list()

dstat_read = list()
dstat_write = list()
dstat_run = list()
dstat_new = list()
dstat_load1 = list()
dstat_load5 = list()
dstat_load15 = list()
dstat_pos = list()
dstat_lck = list()
dstat_rea = list()
dstat_wri = list()
dstat_cpu = list()
c2 = 0

file = open("dstat.log", "r") 

for line in file: 
	line = line.replace("M"," ")
	line = line.replace("G"," ")
	line = line.replace("k"," ") 
	line = line.replace("|"," ")
	line_arr = line.split()

	if len(line_arr) > 6:

		
		dstat_idl.append(float(line_arr[4])) # idl
		dstat_sys.append(float(line_arr[3])) # sys
		dstat_usr.append(float(line_arr[2])) #usr
		dstat_sig.append(float(line_arr[7])) # sig
		dstat_used.append(float(line_arr[8])) # used
		dstat_free.append(float(line_arr[11])) # free
		dstat_buff.append(float(line_arr[9])) # buff
		dstat_cach.append(float(line_arr[10])) # cach
		dstat_read.append(float(line_arr[12])) # read
		dstat_write.append(float(line_arr[13])) # write
		dstat_run.append(float(line_arr[14])) # run
		dstat_new.append(float(line_arr[16])) # new
		dstat_load1.append(float(line_arr[17])) # load1
		dstat_load5.append(float(line_arr[18])) # load5
		dstat_load15.append(float(line_arr[19])) # load15
		dstat_pos.append(float(line_arr[20])) # pos
		dstat_lck.append(float(line_arr[21])) # lck
		dstat_rea.append(float(line_arr[22])) # rea
		dstat_wri.append(float(line_arr[23])) # wri
		dstat_cpu.append(float(line_arr[25])) # cpu
		c2 += 1
	

file.close()

print()
print("DSTAT amount : " + str(c2))
print("READ : " + str(sum(dstat_read)))
print("WRITE : " + str(mean(dstat_write)))
print("RUN : " + str(mean(dstat_run)))
print("NEW : " + str(mean(dstat_new)))
print("LOAD1 : " + str(mean(dstat_load1)))
print("LOAD2 : " + str(mean(dstat_load5)))
print("LOAD3 : " + str(mean(dstat_load15)))
print("POS : " + str(mean(dstat_pos)))
print("LOCK : " + str(mean(dstat_lck)))
print("Read : " + str(mean(dstat_rea)))
print("Write : " + str(mean(dstat_wri)))
print("CPU : " + str(mean(dstat_cpu)))
print("IDLE : " + str(mean(dstat_idl)))
print("SYS : " + str(mean(dstat_sys)))
print("USER : " + str(mean(dstat_usr)))
print("SIG : " + str(mean(dstat_sig)))
print("USED : " + str(mean(dstat_used)))
print("FREE : " + str(mean(dstat_free)))
print("BUFF : " + str(mean(dstat_buff)))
print("CACH : " + str(mean(dstat_cach)))

	

