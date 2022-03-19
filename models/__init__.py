#!/usr/bin/python3
"""
Instantiation file that starts the file storage system
"""
from models.engine import file_storage
from .base_model import BaseModel




storage = file_storage.FileStorage()
storage.reload()
