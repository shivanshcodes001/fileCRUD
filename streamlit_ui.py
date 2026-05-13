import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="CRUD File Manager", layout="centered")

st.title("📁 CRUD File & Folder Manager")

# ---------------- FUNCTIONS ---------------- #

def readfileandfolder():
    p = Path('')
    items = list(p.rglob('*'))

    if items:
        st.subheader("Files & Folders")
        for index, file in enumerate(items):
            st.write(f"{index+1} - {file}")
    else:
        st.info("No files or folders found.")


def create_file(file_name, content):
    p = Path(file_name)

    if p.exists():
        st.warning("FILE ALREADY EXISTS")
    else:
        with open(file_name, 'w') as file:
            file.write(content)
        st.success("FILE ADDED!")


def read_file(file_name):
    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            content = file.read()
        st.text_area("File Content", content, height=200)
    else:
        st.error("FILE NOT FOUND!")


def update_file(file_name, content, mode):
    p = Path(file_name)

    if p.exists():

        if mode == "Overwrite":
            with open(file_name, 'w') as file:
                file.write(content)

        elif mode == "Append":
            with open(file_name, 'a') as file:
                file.write(content)

        st.success("CONTENT UPDATED!")

    else:
        st.error("FILE DOES NOT EXIST!")


def delete_file(file_name):
    p = Path(file_name)

    if p.exists():
        os.remove(p)
        st.success("FILE DELETED")
    else:
        st.error("FILE DOES NOT EXIST!")


def rename_file(file_name, new_name):
    p = Path(file_name)

    if p.exists():
        p.rename(new_name)
        st.success("FILE RENAMED!")
    else:
        st.error("FILE NOT FOUND!")


def create_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        st.warning("FOLDER ALREADY EXISTS!")
    else:
        p.mkdir()
        st.success("FOLDER CREATED!")


def delete_folder(folder_name):
    p = Path(folder_name)

    if p.exists():
        p.rmdir()
        st.success("FOLDER DELETED!")
    else:
        st.error("FOLDER NOT FOUND!")


# ---------------- UI ---------------- #

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "View Files/Folders",
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# View
if menu == "View Files/Folders":
    readfileandfolder()

# Create File
elif menu == "Create File":
    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):
        create_file(file_name, content)

# Read File
elif menu == "Read File":
    file_name = st.text_input("Enter file name")

    if st.button("Read File"):
        read_file(file_name)

# Update File
elif menu == "Update File":
    file_name = st.text_input("Enter file name")
    mode = st.radio("Choose Update Mode", ["Overwrite", "Append"])
    content = st.text_area("Enter new content")

    if st.button("Update File"):
        update_file(file_name, content, mode)

# Delete File
elif menu == "Delete File":
    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):
        delete_file(file_name)

# Rename File
elif menu == "Rename File":
    file_name = st.text_input("Current file name")
    new_name = st.text_input("New file name")

    if st.button("Rename File"):
        rename_file(file_name, new_name)

# Create Folder
elif menu == "Create Folder":
    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):
        create_folder(folder_name)

# Delete Folder
elif menu == "Delete Folder":
    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):
        delete_folder(folder_name)
    