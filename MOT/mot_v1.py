from sys import modules as sys_modules
from customtkinter import *
from pypdf import *
from tkinterDnD import *


def main(text):
    # get each word of text
    words = []
    for word in text.split(" "):
        if word.strip("!?.':;").strip('"') != "":
            words.append(word.strip("!?.':;").strip('"'))

    # add number of occurences to dict
    occurences = {}
    dictKeys = occurences.keys()
    for word in words:
        if word in dictKeys:
            occurences[word] += 1
        else:
            occurences.update({word: 1})
    
    # make dict to list
    occurences = [(item, occurences[item]) for item in occurences]

    return occurences

def pdf_reader(pdf_name):
    reader = PdfReader(pdf_name)