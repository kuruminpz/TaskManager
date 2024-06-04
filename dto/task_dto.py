from flask_restx import Namespace, fields

class TaskDTO:
    api = Namespace('tasks', description='Operações relacionadas a tarefas')

    task_post = api.model('task',{
        'title': fields.String(nullable=False, description='task title'),
        'description':fields.String(nullable=False, description='task description'),
        'end_date': fields.DateTime(nullable=True, description='task end date'),
        'start_date': fields.DateTime(nullable=False, description='task start date'),
        'status': fields.String(nullable=False, description='task status')
        })

    task = api.model('task',{
        'id': fields.Integer(description="task id"),
        'title': fields.String(required=True, description='task title'),
        'description':fields.String(required=True, description='task description'),
        'end_date': fields.DateTime(required=True, description='task end date'),
        'status': fields.String(required=True, description='task status')
    })

  # TODO: add task_update DTO