from PyPDF2 import PdfMerger

def merge_pdfs(files, output):
    merger = PdfMerger()
    
    for file in files:
        merger.append(file)

    merger.write(output)
    merger.close()
    print("Merged successfully!")

if __name__ == "__main__":
    files = ["file1.pdf", "file2.pdf"]
    merge_pdfs(files, "merged.pdf")
