import os
import io

# <---------UPDATE the 'dataset_location' with the directory location of the dataset ------>
dataset_location = "/Users/shamim/Downloads/K8s_inspection/" # Update this LINE such as "/Users/Xyz/Downloads"
#----------------------------------------------------------------------------------------#


github_dataset = "/GITHUB_REPOS"
gitlab_dataset = "/GITLAB_REPOS"

github_data= dataset_location+github_dataset
gitlab_data= dataset_location+gitlab_dataset

yaml_data = open("github_yaml_data.txt", "w")

for (dirpath, dirname, filenames) in os.walk(github_data,topdown=True):
    for filename in filenames:
        #print(filename)
        if filename.endswith((".yaml",".yml")) and not filename.endswith("docker-compose.yml"):
            print(filename)
            filepath = os.path.join(dirpath, filename)
            relpath = os.path.relpath(filepath, dataset_location)
            relpath_repo = os.path.relpath(filepath, github_data)
            #print(relpath)
            repo_name = relpath_repo.split('/')

            yaml_data.write("\n"+"==" * 7 + "Repository Name" + "==" * 7)
            print("\n", repo_name[0], file=yaml_data)
            original_file_name, file_extension = os.path.splitext(filename)
            yaml_data.write("\n"+"=="*7+"File path"+"=="*7)
            print("\n",relpath, file=yaml_data)

            with io.open(filepath, 'r') as f:
                code_content = f.read()
                yaml_data.write("\n"+"=="*7+"File Contents"+"=="*7+"\n\n")
                yaml_data.write(code_content+"\n\n")
                yaml_data.write("=="*20)