import sys
sys.path.append(".")
from app.main_worker import my_tutorial_app
my_tutorial_app.send_task('add', args=[10,5], task_id="my-uuid-123")
