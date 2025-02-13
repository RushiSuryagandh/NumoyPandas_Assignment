import pandas as pd

# Save the results to CSV using pandas DataFrame
def save_to_csv(data, file_name='news_results_2.csv'):
    df = pd.DataFrame(data, columns=["search_content", "search_engine",  "link_of_news", "title", "timestamp", "media_name"])
    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'Data successfully saved in {file_name}')

