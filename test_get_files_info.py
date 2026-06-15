import os
from functions.get_files_info import get_files_info


def execute_get_files_info(working_directory: str, directory: str):
    returnedMessage = get_files_info(working_directory,directory)
    print(f"Result for '{directory}' directory:")
    if "Success:" in returnedMessage:
        # print(os.listdir(working_directory))
        directory_to_work_with = os.path.join(working_directory,directory)
        for directory in os.listdir(directory_to_work_with):
            target = os.path.join(directory_to_work_with,directory)
            print(f" - {directory}: file_size={os.path.getsize(target)}, is_dir={os.path.isdir(target)}")
    else:
        print("   "+returnedMessage)

execute_get_files_info("calculator",".")
execute_get_files_info("calculator","pkg")
execute_get_files_info("calculator","/bin")
execute_get_files_info("calculator", "../")




