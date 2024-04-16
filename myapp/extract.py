import pandas as pd
from pyresparser import ResumeParser
from io import BytesIO
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


# def extract_data(path):
def extract_data(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    return data


def processing(uploaded_files):
    scraped_data = []
    for i in range(len(uploaded_files)):
        file_path = uploaded_files[i]
        inf = extract_data(file_path)
        scraped_data.append(inf)

    data = {
        'name': [str(item['name']) for item in scraped_data],
        'email_id': [str(item['email']) for item in scraped_data],
        'phone_num': [str(item['mobile_number']) for item in scraped_data],
        'skills': [str(item['skills']) for item in scraped_data],
        'college': [str(item['college_name']) for item in scraped_data],
        'degree': [str(item['degree']) for item in scraped_data],
        'designation': [str(item['designation']) for item in scraped_data],
        'experience': [str(item['experience']) for item in scraped_data]
    }

    df = pd.DataFrame(data)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    excel_data = output.getvalue()
    return excel_data