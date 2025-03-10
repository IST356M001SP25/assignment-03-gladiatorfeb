'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''


import streamlit as st
import re
import json

def parse_package_data(data):
    """Parses a single package string and returns structured details."""
    match = re.findall(r'(\d+)\s*(\w+)', data, re.IGNORECASE)
    package_info = {key: int(value) for value, key in match}

    
    total_size = 1
    for value in package_info.values():
        total_size *= value

    return package_info, total_size

st.title(" Process Package Files")


uploaded_files = st.file_uploader("Upload package files:", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    total_lines_processed = 0
    file_count = 0

    for uploaded_file in uploaded_files:
        file_contents = uploaded_file.read().decode("utf-8").strip()
        package_lines = file_contents.split("\n")

        parsed_packages = []

        for line in package_lines:
            package_info, total_size = parse_package_data(line)
            parsed_packages.append({
                "description": line,
                "package_info": package_info,
                "total_size": total_size
            })

        
        json_filename = uploaded_file.name.replace(".txt", ".json")
        with open(json_filename, "w") as json_file:
            json.dump(parsed_packages, json_file, indent=4)

        
        st.info(f" {len(parsed_packages)} packages written to **{json_filename}**")
        
        total_lines_processed += len(parsed_packages)
        file_count += 1

    
    st.success(f" {file_count} files processed, {total_lines_processed} total lines processed")
