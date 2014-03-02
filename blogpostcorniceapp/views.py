""" Cornice services.
"""
from cornice import Service
from blogpostcorniceapp.models import Task
from blogpostcorniceapp.models import DBSession


tasks = Service(name='tasks', path='/tasks', description="Tasks")

@tasks.get()
def get_info(request):
    """Returns a list of all tasks."""
    return {'tasks': [task.name for task in DBSession.query(Task)]}

@tasks.post()
def create_task(request):
    """Adds a new task."""
    task = request.json
    num_existing = DBSession.query(Task).filter(Task.name==task['name']).count()
    if num_existing > 0:
        raise Exception('That task already exists!')
    DBSession.add(Task.from_json(task))


