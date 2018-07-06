# django default
from django.urls import path
from django.conf.urls import url

# swagger
from rest_framework_swagger.views import get_swagger_view

# drf
from .djangoapps.drf.views import SampleView
from .djangoapps.drf.views import SimpleUserView
from .djangoapps.drf.views import SimpleUserAddView

# sample
from .djangoapps.sample import views as SampleViews

#login / logout
from .djangoapps.login import views as LoginViews
from .djangoapps.logout import views as LogoutViews

# side menu
from .djangoapps.main import views as MainViews
from .djangoapps.conference import views as ConferenceViews
from .djangoapps.monitoring import views as MonitoringViews
from .djangoapps.statistics import views as StatisticsViews
from .djangoapps.system import views as SystemViews
from .djangoapps.environment import views as EnvironmentViews
from .djangoapps.supplementaryService import views as SupplementaryServiceViews
from .djangoapps.streamService import views as StreamServiceViews
from .djangoapps.sparkTest import views as SparkTestViews
from .djangoapps.common.lang import views as LangViews
from .djangoapps.common.board import views as BoardViews
from .djangoapps.common.util import views as UtilViews
from .djangoapps.common.core import views as CoreViews

schema_view = get_swagger_view(title='happy API')

urlpatterns = [
    # rest-api
    url('api_sample$', SampleView.as_view()),
    url('api_simpleUser$', SimpleUserView.as_view()),
    url('api_simpleAddUser$', SimpleUserAddView.as_view()),

    # rest-swagger
    url('swagger$', schema_view),

    # sample
    url('sample$', SampleViews.sample, name='sample'),
    url('sample2$', SampleViews.sample2, name='sample2'),
    url('apiTest$', SampleViews.apiTest, name='apiTest'),
    url('vuejs$', SampleViews.vuejs, name='vuejs'),
    url('vueService$', SampleViews.vueService, name='vueService'),

    # board
    url('commList$', BoardViews.commList, name='commList'),

    # Lang API
    url('transLang$', LangViews.transLang, name='transLang'),

    # util
    url('fileUpload$', UtilViews.fileUpload, name='fileUpload'),

    # core
    url('ccChange$', CoreViews.ccChange, name='ccChange'),
    url('envChange$', CoreViews.envChange, name='envChange'),

    # login / logout
    url('login$', LoginViews.login, name='login'),
    url('logout$', LogoutViews.logout, name='logout'),

    # conference
    url('conferenceRoom$', ConferenceViews.conferenceRoom, name='conferenceRoom'),
    url('conferenceRoom/add$', ConferenceViews.conferenceRoomAdd, name='conferenceRoomAdd'),
    url('conferenceRoom/detail$', ConferenceViews.conferenceRoomDetail, name='conferenceRoomDetail'),
    url('conferenceRoom/update$', ConferenceViews.conferenceRoomUpdate, name='conferenceRoomUpdate'),
    url('conferenceRoom/del', ConferenceViews.conferenceRoomDel, name='conferenceRoomDel'),
    url('activeCall$', ConferenceViews.activeCall, name='activeCall'),
    url('activecall_monitoring$', ConferenceViews.activecall_monitoring, name='activecall_monitoring'),
    url('template$', ConferenceViews.template, name='template'),
    url('template/add$', ConferenceViews.templateAdd, name='templateAdd'),
    url('template/detail$', ConferenceViews.templateDetail, name='templateDetail'),
    url('template/update$', ConferenceViews.templateUpdate, name='templateUpdate'),
    url('template/del$', ConferenceViews.templateDel, name='templateDel'),
    url('reserveConference$', ConferenceViews.reserveConference, name='reserveConference'),
    url('reserveConferenceCal$', ConferenceViews.reserveConferenceCal, name='reserveConferenceCal'),

    # monitoring
    url('callStatus$', MonitoringViews.callStatus, name='callStatus'),
    url('networkStatus$', MonitoringViews.networkStatus, name='networkStatus'),
    url('systemStatus$', MonitoringViews.systemStatus, name='systemStatus'),
    url('all_status$', MonitoringViews.all_status, name='all_status'),

    # monitoring
    url('roomUseState$', StatisticsViews.roomUseState, name='roomUseState'),
    url('conferenceStatistics$', StatisticsViews.conferenceStatistics, name='conferenceStatistics'),
    url('periodStatistics$', StatisticsViews.periodStatistics, name='periodStatistics'),

    # system
    url('cdr$', SystemViews.cdr, name='cdr'),
    url('cdr_add$', SystemViews.cdr_add, name='cdr_add'),
    url('cdr_detail$', SystemViews.cdr_detail, name='cdr_detail'),
    url('cdr_del$', SystemViews.cdr_del, name='cdr_del'),
    url('ldap$', SystemViews.ldap, name='ldap'),
    url('account$', SystemViews.account, name='account'),
    url('account_del$', SystemViews.account_del, name='account_del'),
    url('account_detail$', SystemViews.account_detail, name='account_detail'),
    url('account_update$', SystemViews.account_update, name='account_update'),
    url('endPoint$', SystemViews.endPoint, name='endPoint'),
    url('endPoint_detail$', SystemViews.endPoint_detail, name='endPoint_detail'),
    url('endPoint_del$', SystemViews.endPoint_del, name='endPoint_del'),
    url('endPoint_update$', SystemViews.endPoint_update, name='endPoint_update'),
    url('endPointGroup$', SystemViews.endPointGroup, name='endPointGroup'),
    url('endPointGroup_add$', SystemViews.endPointGroup_add, name='endPointGroup_add'),
    url('endPointGroup_del$', SystemViews.endPointGroup_del, name='endPointGroup_del'),
    url('acanoClient$', SystemViews.acanoClient, name='acanoClient'),
    url('logoManagement$', SystemViews.logoManagement, name='logoManagement'),
    url('commandManagement$', SystemViews.commandManagement, name='commandManagement'),

    # environment
    url('environment$', EnvironmentViews.environment, name='environment'),
    url('license$', EnvironmentViews.license, name='license'),

    # supplementary service
    url('outBoundDialPlan$', SupplementaryServiceViews.outBoundDialPlan, name='outBoundDialPlan'),

    # stream service
    url('liveVod$', StreamServiceViews.liveVod, name='liveVod'),
    url('trafficStatistics$', StreamServiceViews.trafficStatistics, name='trafficStatistics'),
    url('conversionStatistics$', StreamServiceViews.conversionStatistics, name='conversionStatistics'),
    url('serverMonitoring$', StreamServiceViews.serverMonitoring, name='serverMonitoring'),
    url('recording$', StreamServiceViews.recording, name='recording'),

    # spark test
    url('spark$', SparkTestViews.spark, name='spark'),
    url('speech$', SparkTestViews.speech, name='speech'),

    # index
    url('$', MainViews.main, name='main'),
]
