from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

# Move the choices outside of the Event class to make them accessible globally
EVENT_TYPE_CHOICES = [
    ('IIC-Calender Activity', 'IIC-Calender Activity'),
    ('Self-Driven Activity', 'Self-Driven Activity'),
    ('Celebration Activity', 'Celebration Activity'),
    # Add more choices as needed
]

THEME_CHOICES = [
    ('general', 'General'),
    ('technology', 'Technology'),
    ('education', 'Education'),
    # Add more choices as needed
]

QUARTER_CHOICES = [
    ('Q1', 'Q1'),
    ('Q2', 'Q2'),
    ('Q3', 'Q3'),
    ('Q4', 'Q4'),
]

CATEGORY_CHOICES = [
    ('seminar', 'Seminar'),
    ('webinar', 'Webinar'),
    ('Paper Presentation', 'Paper Presentation'),
    # Add more choices as needed
]

MODE_CHOICES = [
    ('in_person', 'In-person'),
    ('virtual', 'Virtual'),
    ('hybrid', 'Hybrid'),
]

PLATFORM_CHOICES = [
    ('youtube', 'YouTube'),
    ('instagram', 'Instagram'),
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
]

# Custom Enum Fields
class UserType(models.TextChoices):
    USER = 'User'
    REVIEWER = 'Reviewer'
    ADMIN = 'Admin'
    SUPERADMIN = 'SuperAdmin'

class ApprovalRole(models.TextChoices):
    REVIEWER = 'Reviewer'
    ADMIN = 'Admin'

class EventStatus(models.TextChoices):
    DRAFT = 'Draft'
    PENDING_APPROVAL = 'Pending Approval'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    COMPLETED = 'Completed'

class ReviewStatus(models.TextChoices):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

class Priority(models.TextChoices):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

class DocumentType(models.TextChoices):
    BROCHURE = 'Brochure'
    SCHEDULE = 'Schedule'
    ATTENDANCE_SHEET = 'Attendance Sheet'
    GUEST_DETAIL = 'Guest Detail'
    PHOTO_1 = 'Photo 1'
    PHOTO_2 = 'Photo 2'
    VIDEO_URL = 'Video URL'
    PROMOTIONAL_URL = 'Promotional URL'
    FINAL_REPORT = 'Final Report'

class EventAction(models.TextChoices):
    CREATED = 'Created'
    UPDATED = 'Updated'
    PROOF_UPLOADED = 'Proof Uploaded'
    REVIEWED = 'Reviewed'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    COMPLETED = 'Completed'


# Models
class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=UserType.choices, default=UserType.USER)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ApprovalStage(models.Model):
    stage_order = models.IntegerField()
    stage_name = models.CharField(max_length=255)
    role_required = models.CharField(max_length=20, choices=ApprovalRole.choices)

    def __str__(self):
        return self.stage_name


class Event(models.Model):
    title = models.CharField(max_length=255, default="Untitled Event")
    event_type = models.CharField(max_length=100, choices=EVENT_TYPE_CHOICES, default='conference')
    theme = models.CharField(max_length=255, choices=THEME_CHOICES, default='general')
    quarter = models.CharField(max_length=10, choices=QUARTER_CHOICES, default='Q1')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='academic')
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='in_person')
    objective = models.CharField(max_length=150, default="Not specified")
    outcome = models.CharField(max_length=100, default="Not specified")
    start_date = models.DateField(default="2024-01-01")
    end_date = models.DateField(default="2024-12-31")
    students = models.IntegerField(default=60)
    faculty = models.IntegerField(default=10)
    external_participants = models.IntegerField(default=60)
    duration = models.IntegerField(default=60)
    expenditure = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activity_guide = models.FileField(upload_to='activity_guides/', blank=True, null=True)

class EventProof(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50, choices=DocumentType.choices)
    file_reference = models.FileField(upload_to='media/proofs/', blank=True, null=True)
    url_reference = models.URLField(blank=True, null=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    version = models.IntegerField(default=1)
    
    # New fields for platforms
    video_platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True, null=True)
    promotional_platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.event.title} - {self.document_type}"


'''class EventProof(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50, choices=DocumentType.choices)
    file_reference = models.FileField(upload_to='media/proofs/', blank=True, null=True)
    url_reference = models.URLField(blank=True, null=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    version = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.event.title} - {self.document_type}"
'''

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    approval_stage = models.ForeignKey(ApprovalStage, on_delete=models.SET_NULL, null=True)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=ReviewStatus.choices, default=ReviewStatus.PENDING)
    comments = models.TextField(null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    submission_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Review of {self.event.title} by {self.reviewer.username}"

class EventHistory(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=EventAction.choices)
    performed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.event.title} - {self.action} by {self.performed_by.username}"

class FacultyMember(models.Model):
    sl_no = models.IntegerField(editable=False)  # Make it non-editable
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    designation_and_address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.sl_no:  # Only set the sl_no if it's not already set
            last_sl_no = FacultyMember.objects.aggregate(models.Max('sl_no'))['sl_no__max']
            self.sl_no = 1 if last_sl_no is None else last_sl_no + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sl_no}: {self.name} - {self.category}"

class StudentMember(models.Model):
    sl_no = models.IntegerField(editable=False)  # Make it non-editable
    name_of_student = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.sl_no:  # Only set the sl_no if it's not already set
            last_sl_no = StudentMember.objects.aggregate(models.Max('sl_no'))['sl_no__max']
            self.sl_no = 1 if last_sl_no is None else last_sl_no + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sl_no}: {self.name_of_student} - {self.role}"
