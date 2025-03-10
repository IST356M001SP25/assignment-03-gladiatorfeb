'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import re

def parse_package_data(data):
    """Parses package data string and returns structured package details."""
    match = re.findall(r'(\d+)\s*(eggs|cartons|box)', data, re.IGNORECASE)
    package_info = {key: int(value) for value, key in match}

    
    eggs_per_carton = package_info.get("eggs", 0)
    cartons_per_box = package_info.get("cartons", 1)  
    total_eggs = eggs_per_carton * cartons_per_box

    return package_info, total_eggs


st.title("Process One Package")


package_data = st.text_input("Enter package data:", "12 eggs in 1 carton / 3 cartons in 1 box")

if package_data:
    package_info, total_eggs = parse_package_data(package_data)

    
    for key, value in package_info.items():
        st.markdown(f"**{key.capitalize()}** ➡ {value}")

    
    st.success(f"**Total  Size:** {total_eggs} eggs")
