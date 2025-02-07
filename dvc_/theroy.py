# DVC -> 
# DVC can only be used to tracking data and model versions
# DVC can be worked with github for commiting and dvc doesnt provide that feature of commiting like github 
# install dvc using -> pip install dvc
# initialize dvc -> dvc init
# create data.txt -> commit in git 

# run dvc add data/data.txt -> now this will be tracked by dvc and not git -> .gitignore is created and there will be data.txt file in that file so that git will not track it 


# data.txt.dvc -> will get created in dvc file so that it can be tracked using hash key which maps the actual data.txt file 
# and the git will only track the dvc file where hash of data.txt is present and not the exact data.txt file where data is present


#  so track or add -> data.txt.dvc -> git add data/data.txt.dvc
# also track/ add -> git add data/.ignore

# now if content of dvc got change the hash key mapped to it will also got changed



# to checkout files first do git checkout file_hash
# and to checkout the previous version checkout using dvc checkout


# and to swith to current branch => git checkout master
# then do dvc checkout