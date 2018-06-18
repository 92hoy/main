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

    # Lang API
    url('transLangEN$', LangViews.transLangEN, name='transLangEN'),
    url('transLangKO$', LangViews.transLangKO, name='transLangKO'),
    url('transLangJP$', LangViews.transLangJP, name='transLangJP'),

    # login / logout
    url('login$', LoginViews.login, name='login'),
    url('logout$', LogoutViews.logout, name='logout'),

    # conference
    url('conferenceRoom$', ConferenceViews.conferenceRoom, name='conferenceRoom'),
    url('activeCall$', ConferenceViews.activeCall, name='activeCall'),
    url('template$', ConferenceViews.template, name='template'),
    url('reserveConference$', ConferenceViews.reserveConference, name='reserveConference'),
    url('reserveConferenceCal$', ConferenceViews.reserveConferenceCal, name='reserveConferenceCal'),

    # monitoring
    url('callStatus$', MonitoringViews.callStatus, name='callStatus'),
    url('networkStatus$', MonitoringViews.networkStatus, name='networkStatus'),
    url('systemStatus$', MonitoringViews.systemStatus, name='systemStatus'),

    # monitoring
    url('roomUseState$', StatisticsViews.roomUseState, name='roomUseState'),
    url('conferenceStatistics$', StatisticsViews.conferenceStatistics, name='conferenceStatistics'),
    url('periodStatistics$', StatisticsViews.periodStatistics, name='periodStatistics'),

    # system
    url('cdr$', SystemViews.cdr, name='cdr'),
    url('ldap$', SystemViews.ldap, name='ldap'),
    url('account$', SystemViews.account, name='account'),
    url('endPoint$', SystemViews.endPoint, name='endPoint'),
    url('endPointGroup$', SystemViews.endPointGroup, name='endPointGroup'),
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
