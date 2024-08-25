from django.db import models

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
