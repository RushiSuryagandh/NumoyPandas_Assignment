import time
# Decorator function to calculate execution time
def execution_time(func):
    async def wrapper(*args,**kwargs):
        start_time=time.time()
        result=await func(*args,**kwargs)
        end_time=time.time()
        print(f'Execution time :{end_time-start_time}')
        return result
    return wrapper