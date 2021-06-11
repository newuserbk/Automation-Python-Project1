import csv
import openpyxl


def getRowCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return (sheet.max_row)


def getColumnCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return (sheet.max_column)


def readData(file, sheetName, rownum, columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(row=rownum, column=columnno).value


def writeData(file, sheetName, rownum, columnno, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    sheet.cell(row=rownum, column=columnno).value = data
    workbook.save(file)


def getCSVData(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
