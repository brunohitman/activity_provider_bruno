# GET.py
from flask import jsonify
from get_command import GetCommand

# Função para lidar com requisições GET
def get_example():
    get_command = GetCommand()
    return get_command.execute()
