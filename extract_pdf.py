import fitz  # PyMuPDF
import os
import sys

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num, page in enumerate(doc, 1):
            text += f"\n--- Page {page_num} ---\n"
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        return f"Error extracting {pdf_path}: {str(e)}"

def main():
    pdf_dir = r"d:\projects\os otes\pdf"
    
    # Process each day folder
    for day_folder in sorted(os.listdir(pdf_dir)):
        day_path = os.path.join(pdf_dir, day_folder)
        if not os.path.isdir(day_path):
            continue
            
        print(f"\n{'='*60}")
        print(f"Processing {day_folder}")
        print('='*60)
        
        # Process each PDF in the day folder
        for pdf_file in sorted(os.listdir(day_path)):
            if pdf_file.lower().endswith('.pdf'):
                pdf_path = os.path.join(day_path, pdf_file)
                print(f"\n--- {pdf_file} ---")
                
                text = extract_pdf_text(pdf_path)
                
                # Save to text file
                txt_path = pdf_path.replace('.pdf', '.txt').replace('.PDF', '.txt')
                with open(txt_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Saved to: {txt_path}")

if __name__ == "__main__":
    main()
