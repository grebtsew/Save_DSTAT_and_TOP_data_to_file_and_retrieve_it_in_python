from subprocess import call
import video
import threading


# Samples


#Start program
t1 = threading.Thread(target=video.start)
t1.start()

#call(["python3", "main\\-\\ownedit_video.py"])

# Run dstat

#call(["dstat", "--time", "--cpu","--cpufreq", "--mem","--disk", "-power", "--load", "--proc", "--#lock", "--vm", "--unix", "--output", "tmp/dstat.log"])

#dstat --time --cpu --cpufreq --mem --disk -power --load --proc --lock --vm --unix --top-cpu --output tmp/dstat.log | grep python3

# Run top
#call(["top", "-b", ">", "tmp/top.txt"])

#top -b > tmp/top.txt | grep python3

#call(["sudo","intel_gpu_top", "-b", ">", "tmp/top_gpu.txt"])

#sudo intel_gpu_top > tmp/top_gpu.txt


#RUN THESE:
#python3 start.py
#dstat --time --cpu --mem  --disk -power --load --lock  --top-cpu  | grep --line-buffered python3 > tmp/dstat.log 
#top -b | grep --line-buffered "python3" > tmp/top.txt 


