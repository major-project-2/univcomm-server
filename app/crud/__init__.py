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
from .crud_announcement import announcement
from .crud_announcement_file import announcement_file
from .crud_post_file import post_file
from .crud_question_file import question_file
from .crud_hand_raise import hand_raise
from .crud_upvote import upvote
from .crud_downvote import downvote

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.post import Post
# from app.schemas.post import PostCreate, PostUpdate

# post = CRUDBase[Post, PostCreate, PostUpdate]
