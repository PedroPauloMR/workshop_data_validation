from frontend import ExcelValidadorUI
from backend import process_excel


def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        result, erros = process_excel(upload_file)
        ui.displauy_results(result, erros)


if __name__ == '__main__':
    main()