from flask import request
from flask_restx import Namespace, Resource, fields
from model.task_model import Task
from app import db


# TODO: make task request controllers. AFTER: task services