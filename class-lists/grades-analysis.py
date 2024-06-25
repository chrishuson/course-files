import pandas as pd
from tabula import read_pdf

# Step 3: Read Data from PDF
pdf_path = 'allteachers.pdf'
df_list = read_pdf(pdf_path, pages='all', multiple_tables=True)

# Step 4: Combine DataFrames (Optional)
df = pd.concat(df_list, ignore_index=True)

# Step 5: Clean and Format the DataFrame
#df.columns = ['Column1', 'Column2', 'Column3']

# Step 6: Export to Excel
#excel_path = 'path/to/your/output.xlsx'
#df.to_excel(excel_path, index=False)