# Save_DSTAT_and_TOP_data_to_file_and_retrieve_it_in_python
Show how to save dstat and top data to a file. Then retrieve the data from the created file in python. Finally calculate mean values. Data in this example comes from an evaluation of tensorflow modells.

# HOW?
Run get_data.py from each folder containing a top.txt and a dstat.log

# Note
".log" files are ignored...

# RUN THESE TO SAVE EVALUATION DATA TO FILE:
python3 start.py # Start program
dstat --time --cpu --mem  --disk -power --load --lock  --top-cpu  | grep --line-buffered python3 > tmp/dstat.log 
top -b | grep --line-buffered "python3" > tmp/top.txt 
