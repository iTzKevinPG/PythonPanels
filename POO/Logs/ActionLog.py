import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode='a', filename='app.log')

def save_log(func):

    def wrapper_save_log(*args, **kwargs):
            
        arg = func(*args, **kwargs)

        logging.warning(f"El usuario {arg.name} realizo la accion: {arg.actionUser}.")

    return wrapper_save_log







