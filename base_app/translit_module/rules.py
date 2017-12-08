def get_rules(file="./rules.xlsx", sheetname='rules', debug="N"):
    """fill dictionary with rules and return it
    \n  file -
    \n  sheetname -
    \n  debug - option to print debug messages to console (in case debug = 'Y')
    """
    from .helpfull_output import deb_print
    deb_print(debug, "Welcome to 'get_rules()' function")
    result = {}
    # open excel-'file'
    # use excel library 'openpyxl'
    import openpyxl
    try:
        deb_print(debug, 'Opening a file ', file)
        wb = openpyxl.load_workbook(file)
        obj_rules_sheet = wb.get_sheet_by_name(sheetname)
    except Exception as wb_ex:
        deb_print(debug, wb_ex)
    else:
        deb_print(debug, "Found '", obj_rules_sheet.title, "' sheet")
        deb_print(debug, "Adding rules..")
        i = 1
        while obj_rules_sheet.cell(row=i, column=1).value is not None:
            result[obj_rules_sheet.cell(row=i, column=1).value] = \
                obj_rules_sheet.cell(row=i, column=2).value
            i += 1
        deb_print(debug, "Closing the file...")
        wb.close()
    finally:
        deb_print(debug, "Return result. \nEnd of function.\n\n")
        return result
