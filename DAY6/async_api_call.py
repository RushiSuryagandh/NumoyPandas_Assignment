import asyncio
import aiohttp
import time

# Define the decorator for logging execution time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Fetching data \n start time:{start_time} sec \n End time:{end_time} sec \n Total_Execution_time: {end_time-start_time} sec')
        return result
    return wrapper

# Asynchronous function to fetch data from a single API
async def fetch_single_api_data(api, session):
    # print(session)  - the same session for every request
    try:
        async with session.get(api) as response:
            # print(await response.text())
            response.raise_for_status()  # Raises an error 
            result = await response.json()
            return result
    except Exception as e:
        return f"Error fetching data from {api}: {e}"

# Asynchronous function to fetch data from all APIs concurrently
async def fetch_data_from_all_API(apis):
    async with aiohttp.ClientSession() as session:
        # print(session)
        tasks = [fetch_single_api_data(api, session) for api in apis]
        # print(tasks)
        results = await asyncio.gather(*tasks)
        # for result in results:
        #     print(result)
# Wrapper function to measure execution time
@log_execution_time
def main():
    apis = [
        'https://jsonplaceholder.typicode.com/users/6', 
        'https://jsonplaceholder.typicode.com/users/4', 
        'https://jsonplaceholder.typicode.com/todos/19'
    ]
    asyncio.run(fetch_data_from_all_API(apis))# Run async function
    

main()