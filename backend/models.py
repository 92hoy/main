from django.db import models
from django.utils import timezone

# from backend.models import CmsManager
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

# from backend.models import ApiCdrCall
class ApiCdrCall(models.Model):
    session = models.TextField(primary_key=True)
    correlatorindex = models.IntegerField(primary_key=True)
    record_type = models.TextField()
    call_id = models.TextField()
    name = models.TextField()
    calltype = models.TextField()
    cospace = models.TextField()
    callcorrelator = models.TextField()
    calllegscompleted = models.IntegerField()
    calllegsmaxactive = models.IntegerField()
    durationseconds = models.IntegerField()
    add_date = models.DateTimeField()
    cdrtag = models.TextField()
    tenant = models.TextField()
    class Meta:
        managed = False
        db_table = 'api_cdr_call'

# from backend.models import ApiCdrCallleg
class ApiCdrCallleg(models.Model):
    session = models.TextField(primary_key=True)
    correlatorindex = models.IntegerField(primary_key=True)
    record_type = models.TextField()
    callleg_id = models.TextField()
    cdrtag = models.TextField()
    displayname = models.TextField()
    guestconnection = models.TextField()
    localaddress = models.TextField()
    remoteaddress = models.TextField()
    remoteparty = models.TextField()
    recording = models.TextField()
    type = models.TextField()
    subtype = models.TextField()
    lyncsubtype = models.TextField()
    direction = models.TextField()
    call = models.TextField()
    ivr = models.TextField()
    ownerid = models.TextField()
    sipcallid = models.TextField()
    groupid = models.TextField()
    reason = models.TextField()
    remoteteardown = models.TextField()
    encryptedmedia = models.TextField()
    unencryptedmedia = models.TextField()
    durationseconds = models.IntegerField()
    mediausagepercentages_mainvideoviewer = models.FloatField()
    mediausagepercentages_mainvideocontributor = models.FloatField()
    mediausagepercentages_presentationviewer = models.FloatField()
    mediausagepercentages_presentationcontributor = models.FloatField()
    alarm_type = models.TextField()
    alarm_durationpercentage = models.FloatField()
    rxvideo_codec = models.TextField()
    rxvideo_maxsizewidth = models.IntegerField()
    rxvideo_maxsizeheight = models.IntegerField()
    rxvideo_packetlossbursts_duration = models.IntegerField()
    rxvideo_packetlossbursts_density = models.IntegerField()
    rxvideo_packetgap_duration = models.IntegerField()
    rxvideo_packetgap_density = models.IntegerField()
    txvideo_codec = models.TextField()
    txvideo_maxsizewidth = models.IntegerField()
    txvideo_maxsizeheight = models.IntegerField()
    txvideo_packetlossbursts_duration = models.FloatField()
    txvideo_packetlossbursts_density = models.FloatField()
    txvideo_packetgap_duration = models.FloatField()
    txvideo_packetgap_density = models.FloatField()
    rxaudio_codec = models.TextField()
    rxaudio_packetlossbursts_duration = models.FloatField()
    rxaudio_packetlossbursts_density = models.FloatField()
    rxaudio_packetgap_duration = models.FloatField()
    rxaudio_packetgap_density = models.FloatField()
    txaudio_codec = models.TextField()
    txaudio_packetlossbursts_duration = models.FloatField()
    txaudio_packetlossbursts_density = models.FloatField()
    txaudio_packetgap_duration = models.FloatField()
    txaudio_packetgap_density = models.FloatField()
    state = models.TextField()
    deactivated = models.TextField()
    add_date = models.DateTimeField()
    ep_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'api_cdr_callleg'

# from backend.models import ApiCdrRecord
class ApiCdrRecord(models.Model):
    session = models.TextField(primary_key=True)
    correlatorindex = models.IntegerField(primary_key=True)
    type = models.TextField()
    time = models.TextField()
    recordindex = models.IntegerField()
    add_date = models.DateTimeField()
    utc_time = models.DateTimeField()
    local_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'api_cdr_record'

# from backend.models import ApiCdrRecording
class ApiCdrRecording(models.Model):
    session = models.TextField(primary_key=True)
    correlatorindex = models.IntegerField(primary_key=True)
    record_type = models.TextField()
    recording_id = models.TextField()
    path = models.TextField()
    recorderurl = models.TextField()
    call = models.TextField()
    callleg = models.TextField()
    add_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'api_cdr_recording'

# from backend.models import ApiCdrRecords
class ApiCdrRecords(models.Model):
    session = models.TextField(primary_key=True)
    callbridge = models.TextField()
    add_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'api_cdr_records'

# from backend.models import CmsCospace
class CmsCospace(models.Model):
    cospace_seq = models.TextField(primary_key=True)
    cospace_id = models.TextField()
    start_dt = models.DateTimeField()
    passcode = models.TextField()
    call_id = models.TextField()
    bandwidth = models.TextField()
    delete_yn = models.TextField()
    use_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_cospace'

# from backend.models import CmsCospaceControl
class CmsCospaceControl(models.Model):
    cospace_seq = models.IntegerField(primary_key=True)
    cospace_id = models.TextField(primary_key=True)
    id = models.TextField()
    delete_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_cospace_control'

# from backend.models import CmsCospaceDetail
class CmsCospaceDetail(models.Model):
    cospace_id = models.TextField(primary_key=True)
    user_id = models.TextField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'cms_cospace_detail'

# from backend.models import CmsCospaceEndpoint
class CmsCospaceEndpoint(models.Model):
    seq = models.IntegerField(primary_key=True)
    callnumber = models.TextField()
    id = models.TextField()
    type = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_cospace_endpoint'

# from backend.models import CmsCospaceUser
class CmsCospaceUser(models.Model):
    seq = models.IntegerField(primary_key=True)
    userjid = models.TextField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_cospace_user'

# from backend.models import CmsEndpoint
class CmsEndpoint(models.Model):
    ep_id = models.TextField(primary_key=True)
    ep_group_seq = models.TextField()
    ep_name = models.TextField()
    ep_type = models.TextField()
    ip = models.TextField()
    sip = models.TextField()
    username = models.TextField()
    recodingdevice = models.TextField()
    audioonly = models.TextField()
    hdevice = models.TextField()
    mslync = models.TextField()
    gmt_time = models.TextField()
    ep_group_sub_seq = models.TextField()
    order_no = models.IntegerField()
    delete_yn = models.TextField()
    use_yn = models.TextField()
    open_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_endpoint'

# from backend.models import CmsEndpointGroup
class CmsEndpointGroup(models.Model):
    ep_group_seq = models.IntegerField(primary_key=True)
    ep_group_name = models.TextField()
    ep_group_color = models.TextField()
    order_no = models.IntegerField()
    delete_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_endpoint_group'

# from backend.models import CmsLdapserver
class CmsLdapserver(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField()
    password = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_ldapserver'

# from backend.models import CmsResvCospace
class CmsResvCospace(models.Model):
    resv_seq = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField()
    resv_name = models.TextField()
    end_date = models.DateTimeField()
    passcode = models.TextField()
    call_id = models.TextField()
    bandwidth = models.TextField()
    delete_yn = models.TextField()
    use_yn = models.TextField()
    call_yn = models.TextField()
    discon_yn = models.TextField()
    call_uuid = models.TextField()
    cospace_uuid = models.TextField()
    schedule_call_type = models.TextField()
    host_name = models.TextField()
    host_email = models.TextField()
    cospace_type = models.TextField()
    cospace_url = models.TextField()
    duration = models.IntegerField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_resv_cospace'

# from backend.models import CmsResvCospaceEndpoint
class CmsResvCospaceEndpoint(models.Model):
    resv_seq = models.IntegerField(primary_key=True)
    ep_id = models.IntegerField(primary_key=True)
    call_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_resv_cospace_endpoint'

# from backend.models import CmsResvCospaceUser
class CmsResvCospaceUser(models.Model):
    resv_seq = models.IntegerField(primary_key=True)
    userjid = models.TextField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    call_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_resv_cospace_user'

# from backend.models import CmsTemplate
class CmsTemplate(models.Model):
    seq = models.IntegerField(primary_key=True)
    title = models.TextField()
    delete_yn = models.TextField()
    callbrandingprofile = models.TextField()
    calllegprofile = models.TextField()
    callprofile = models.TextField()
    dtmfprofile = models.TextField()
    ivrbrandingprofile = models.TextField()
    userprofile = models.TextField()
    note = models.TextField()
    # regist_date = models.DateTimeField(default=timezone.now)
    regist_date = models.DateTimeField(auto_now_add=True)
    regist_id = models.TextField()
    modify_date = models.DateTimeField(auto_now=True, null=True)
    modify_id = models.TextField()

    def publish(self):
        self.modify_date = timezone.now()
        self.save()
    class Meta:
        managed = False
        db_table = 'cms_template'

# from backend.models import CmsCodeGroup
class CmsCodeGroup(models.Model):
    group_code = models.TextField(primary_key=True)
    group_name = models.TextField()
    group_ename = models.TextField()
    group_note = models.TextField()
    delete_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_code_group'

# from backend.models import CmsCodeDetail
class CmsCodeDetail(models.Model):
    group_code = models.TextField(primary_key=True)
    detail_code = models.TextField(primary_key=True)
    code_name = models.TextField()
    code_ename = models.TextField()
    note = models.TextField()
    ref_code = models.TextField()
    order_no = models.IntegerField()
    delete_yn = models.TextField()
    regist_date = models.DateTimeField()
    regist_id = models.TextField()
    modify_date = models.DateTimeField()
    modify_id = models.TextField()
    class Meta:
        managed = False
        db_table = 'cms_code_detail'

# from backend.models import CmsLoginLog
class CmsLoginLog(models.Model):
    seq = models.IntegerField(primary_key=True)
    user_id = models.TextField()
    login_ip = models.TextField()
    user_agent = models.TextField()
    regist_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'cms_login_log'
