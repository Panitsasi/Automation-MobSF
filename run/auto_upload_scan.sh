
#!/bin/bash

# Check if there are any uploaded files and move them into APKs directory.
if [ -z "$(ls -A ~/Automation-MobSF/run/website/uploads)" ]; 
then
  echo "$(tput setaf 3)MESSAGE: $(tput setaf 7)[There are not any uploaded samples.]"
else
  mv -v ~/Automation-MobSF/run/website/uploads/* ~/Automation-MobSF/APKs
  echo "$(tput setaf 4)MESSAGE: $(tput setaf 7)[Uploaded samples moved into APKS directory.]"
fi
# Supported Android app binaries - APK. Remove any other file extension from APKs directory
find ~/Automation-MobSF/APKs/ -type f ! -name "*.apk";

# Number of samples that I want to scan.
num_samples=$(find ~/Automation-MobSF/APKs/ -type f | wc -l);

# If there are no samples into the APKs file, then print message.
if [[ $num_samples != 0 ]]; 
    then 
    echo "$(tput setaf 1)MESSAGE:$(tput setaf 7) There are $(tput setaf 4) $num_samples samples $(tput setaf 7) to be scanned."

    # Calculate the md5 hash value of each sample and create a txt file whcich contains the md5 and the path of each sample.
    find ~/Automation-MobSF/APKs/ -type f -exec md5sum {} + | sort -k 2 > ~/Automation-MobSF/scans_comparison/samples.txt;

    # Create a txt file which contains all the samples (md5 hash value) which have been already scanned by MobSF.
    ls ~/Mobile-Security-Framework-MobSF/uploads/ > ~/Automation-MobSF/scans_comparison/scanned_samples.txt;
    
    # Authorization API Key.
    api_key=$(head -n 1 ~/Automation-MobSF/authorization_api_key.txt);

    # Loop over the number of samples. 
    for ((num=1; num<= "$num_samples"; num++));
    do
    # From the txt file, I store the values of md5 and path of the sample.
       sample_md5=`sed -n -e "$num"p ~/Automation-MobSF/scans_comparison/samples.txt | awk '{print $1}'`
       sample_path=`sed -n -e "$num"p ~/Automation-MobSF/scans_comparison/samples.txt | awk '{print $2}'`;

    # Check if the sample has already been scanned.
    # If "YES", remove file from those which I want to be scanned. If "NO", continue with scanning.  
    	 if grep -q "${sample_md5}" ~/Automation-MobSF/scans_comparison/scanned_samples.txt;
	    then
	      echo "$(tput setaf 2)MESSAGE: $(tput setaf 4)[SAMPLE HAS BEEN ALREADY SCANNED]"
	      rm "$sample_path";
	      
	    else
	      echo "$(tput setaf 6)START SCANNING THE SAMPLES...";

	      test_sample="${sample_path}"
	      name_sample="${sample_path:35}"
	      type_sample="${sample_path: -3}"

	      # Upload sample.
	      echo "UPLOAD SAMPLE:$(tput setaf 6) STEP 1 OUT OF 6"
	      curl -F "file=@$test_sample" http://localhost:8000/api/v1/upload -H "Authorization:$api_key";

	      # Scan sample. Static Analysis
	      echo
	      echo "STATIC SCAN:$(tput setaf 6) STEP 2 OUT OF 6";
	      static_data=$(curl -X POST --url http://localhost:8000/api/v1/scan --data "scan_type=$type_sample&file_name=$name_sample&hash=$sample_md5" -H "Authorization:$api_key");
              echo "$static_data" > ~/Automation-MobSF/run/static_data.txt;
             
	      # Run script to start Dynamic Analysis
	      echo
	      echo "DYNAMIC SCAN:$(tput setaf 6) STEP 3 OUT OF 6";
	      
	      package_sample=$(python3 ~/Automation-MobSF/run/dynamic_scan.py "$name_sample" 2>&1);

	      # Run script to download Static and Dynamic Report.
	      echo
	      echo "CREATE REPORTS:$(tput setaf 6) STEP 4 OUT OF 6";
	      python3 ~/Automation-MobSF/run/reports.py "$sample_md5" "$package_sample" "$api_key" "$name_sample";

	      # Move Dynamic report to reports directory.
	      mv Dynamic.pdf ~/Automation-MobSF/reports/"$sample_md5"/
	      

	      python3 ~/Automation-MobSF/run/store_reports.py "$sample_md5";
	      echo
	      echo "Access to Database:$(tput setaf 6) STEP 5 OUT OF 6";
	      python3 ~/Automation-MobSF/run/connect.py "$sample_md5" 2>&1 ;

        echo "Binary Classification:$(tput setaf 6) STEP 6 OUT 6";
	      python3 ~/Automation-MobSF/run/classifier.py  ;


	      # Kill emulator, in order to start the new analysis.
	      # The emulator start with wipe-data.
	      adb -s emulator-5554 emu kill;
	      echo "$(tput setaf 3)MESSAGE: $(tput setaf 6) [Kill Emulator & Wait to be Loaded Again.]";
	      sleep 1m;
     fi
   done
else
    echo "$(tput setaf 1)MESSAGE:$(tput setaf 8) [There are no files to be scanned]";
    sleep 1m ;
fi
# Start again after two minutes.
sleep 2m 
