from .crud_user import user
from .crud_role import role
from .crud_student_data import student_data
from .crud_faculty_data import faculty_data
from .crud_alumni_data import alumni_data
from .crud_faculty_experience import faculty_experience
from .crud_alumni_experience import alumni_experience
from .crud_post import post
from .crud_comment import comment
from .crud_question import question
from .crud_answer import answer

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
