import sys
import ezsheets

def convert_to_excel(file_path):
    ss = ezsheets.upload(file_path)
    ss.downloadAsExcel()

def convert_to_ods(file_path):
    ss = ezsheets.upload(file_path)
    ss.downloadAsODS()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_spreadsheet.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    # Excel形式に変換
    convert_to_excel(file_path)
    
    # ODS形式に変換
    convert_to_ods(file_path)

    print(f"File '{file_path}' converted to Excel and ODS,PDF formats.")

