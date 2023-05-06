from .crud_item import item
from .crud_user import user
from .crud_role import role
from .crud_student_data import student_data
from .crud_faculty_data import faculty_data
from .crud_alumni_data import alumni_data

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
