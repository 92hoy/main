from django.db import models

class CmsManager(models.Model):
    user_id = models.TextField(primary_key=True)
    user_pwd = models.TextField()
    user_name = models.TextField()
    user_role = models.TextField()
    pw_change_date = models.DateTimeField()
    login_fail_cnt = models.IntegerField()
    last_login = models.DateTimeField()
    language = models.TextField()
    delete_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'cms_manager'
