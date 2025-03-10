'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
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

st.title("📦 Process File of Packages")


uploaded_file = st.file_uploader("Upload package file:", type=["txt"])

if uploaded_file:
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

        
        st.markdown(f"**{line}** ➡ **Total  Size:** {total_size} {list(package_info.keys())[0]}s")

   
    json_filename = uploaded_file.name.replace(".txt", ".json")
    with open(json_filename, "w") as json_file:
        json.dump(parsed_packages, json_file, indent=4)

    
    st.success(f" {len(parsed_packages)} packages written to **{json_filename}**")
