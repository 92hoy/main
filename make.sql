create table cms_manager(
	`user_id` varchar(50)  not null,
	`user_name` varchar(50)  not null,
	`user_pwd` varchar(100)  not null,
	`user_role` varchar(100)  not null,
	`pw_change_date` datetime default null,
	`login_fail_cnt` int default 0,
	`last_login` datetime default null,
	`language` varchar(20) default 'en',
	`delete_yn` char(1) default 'N',
	`regist_date` datetime default now(),
	`regist_id` varchar(50) default null,
	`modify_date` datetime default null,
	`modify_id` varchar(50) default null,
	primary key(user_id)
);

create table api_cdr_call(
	`session`  varchar(50)   ,
	`correlatorindex`  int   ,
	`record_type`  varchar(100)   ,
	`call_id`  varchar(100)   ,
	`name`  varchar(100)   ,
	`calltype`  varchar(100)   ,
	`cospace`  varchar(100)   ,
	`callcorrelator`  varchar(100)   ,
	`calllegscompleted`  int   ,
	`calllegsmaxactive`  int   ,
	`durationseconds`  int   ,
	`add_date`  datetime   ,
	`cdrtag`  varchar(100)   ,
	`tenant`  varchar(100)   ,
	primary key ( session, correlatorindex )
);

create table api_cdr_callleg(
	`session`  varchar(100)   ,
	`correlatorindex`  int   ,
	`record_type`  varchar(100)   ,
	`callleg_id`  varchar(100)   ,
	`cdrtag`  varchar(100)   ,
	`displayname`  varchar(100)   ,
	`guestconnection`  varchar(100)   ,
	`localaddress`  varchar(100)   ,
	`remoteaddress`  varchar(100)   ,
	`remoteparty`  varchar(100)   ,
	`recording`  varchar(100)   ,
	`type`  varchar(100)   ,
	`subtype`  varchar(100)   ,
	`lyncsubtype`  varchar(100)   ,
	`direction`  varchar(100)   ,
	`call`  varchar(100)   ,
	`ivr`  varchar(100)   ,
	`ownerid`  varchar(100)   ,
	`sipcallid`  varchar(100)   ,
	`groupid`  varchar(100)   ,
	`reason`  varchar(100)   ,
	`remoteteardown`  varchar(100)   ,
	`encryptedmedia`  varchar(100)   ,
	`unencryptedmedia`  varchar(100)   ,
	`durationseconds`  int   ,
	`mediausagepercentages_mainvideoviewer`  double   ,
	`mediausagepercentages_mainvideocontributor`  double   ,
	`mediausagepercentages_presentationviewer`  double   ,
	`mediausagepercentages_presentationcontributor`  double   ,
	`alarm_type`  varchar(100)   ,
	`alarm_durationpercentage`  double   ,
	`rxvideo_codec`  varchar(100)   ,
	`rxvideo_maxsizewidth`  int   ,
	`rxvideo_maxsizeheight`  int   ,
	`rxvideo_packetlossbursts_duration`  double   ,
	`rxvideo_packetlossbursts_density`  double   ,
	`rxvideo_packetgap_duration`  double   ,
	`rxvideo_packetgap_density`  double   ,
	`txvideo_codec`  varchar(100)   ,
	`txvideo_maxsizewidth`  int   ,
	`txvideo_maxsizeheight`  int   ,
	`txvideo_packetlossbursts_duration`  double   ,
	`txvideo_packetlossbursts_density`  double   ,
	`txvideo_packetgap_duration`  double   ,
	`txvideo_packetgap_density`  double   ,
	`rxaudio_codec`  varchar(100)   ,
	`rxaudio_packetlossbursts_duration`  double   ,
	`rxaudio_packetlossbursts_density`  double   ,
	`rxaudio_packetgap_duration`  double   ,
	`rxaudio_packetgap_density`  double   ,
	`txaudio_codec`  varchar(100)   ,
	`txaudio_packetlossbursts_duration`  double   ,
	`txaudio_packetlossbursts_density`  double   ,
	`txaudio_packetgap_duration`  double   ,
	`txaudio_packetgap_density`  double   ,
	`state`  varchar(100)   ,
	`deactivated`  varchar(100)   ,
	`add_date`  datetime   ,
	`ep_id`  varchar(100)   ,
	primary key ( session, correlatorindex )
);


create table api_cdr_record(
	`session`  varchar(100)   ,
	`correlatorindex`  int   ,
	`type`  varchar(100)   ,
	`time`  varchar(100)   ,
	`recordindex`  int   ,
	`add_date`  datetime   ,
	`utc_time`  datetime   ,
	`local_time`  datetime   ,
	primary key ( session, correlatorindex )
);

create table api_cdr_recording(
	`session`  varchar(100)   ,
	`correlatorindex`  int   ,
	`record_type`  varchar(100)   ,
	`recording_id`  varchar(100)   ,
	`path`  varchar(100)   ,
	`recorderurl`  varchar(100)   ,
	`call`  varchar(100)   ,
	`callleg`  varchar(100)   ,
	`add_date`  datetime   ,
	primary key ( session, correlatorindex )
);

create table api_cdr_records(
	`session`  varchar(100)   ,
	`callbridge`  varchar(100)   ,
	`add_date`  datetime   ,
	primary key ( session )
);


create table cms_cospace(
	`cospace_seq`  int  auto_increment ,
	`cospace_id`  varchar(100)   ,
	`start_dt`  datetime   ,
	`passcode`  varchar(100)   ,
	`call_id`  varchar(100)   ,
	`bandwidth`  varchar(100)   ,
	`delete_yn`  varchar(100)   ,
	`use_yn`  varchar(100)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(100)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(100)   ,
	primary key ( cospace_seq )
);

create table cms_cospace_control(
	`cospace_seq`  int   ,
	`cospace_id`  varchar(100)   ,
	`id`  varchar(100)   ,
	`delete_yn`  varchar(100)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(100)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(100)   ,
	primary key ( cospace_seq, cospace_id )
);

create table cms_cospace_detail(
	`cospace_id`  varchar(100)   ,
	`user_id`  varchar(100)   ,
	primary key ( cospace_id, user_id )
);

create table cms_cospace_endpoint(
	`seq`  int   ,
	`callnumber`  varchar(100)   ,
	`id`  varchar(100)   ,
	`type`  varchar(100)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(100)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(100)   ,
	primary key ( seq )
);

create table cms_cospace_user(
	`seq`  int   ,
	`userjid`  varchar(100)   ,
	`name`  varchar(100)   ,
	`email`  varchar(100)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(100)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(100)   ,
	primary key ( seq, userjid )
);

 create table cms_endpoint(
	`ep_id`  varchar(100)   ,
	`ep_group_seq`  varchar(100)   ,
	`ep_name`  varchar(100)   ,
	`ep_type`  varchar(100)   ,
	`ip`  varchar(100)   ,
	`sip`  varchar(100)   ,
	`username`  varchar(100)   ,
	`recodingdevice`  varchar(100)   ,
	`audioonly`  varchar(100)   ,
	`hdevice`  varchar(100)   ,
	`mslync`  varchar(100)   ,
	`gmt_time`  varchar(100)   ,
	`ep_group_sub_seq`  varchar(100)   ,
	`order_no`  int   ,
	`delete_yn`  varchar(100)   ,
	`use_yn`  char(1)   ,
	`open_yn`  char(1)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( ep_id )
);

create table cms_endpoint_group(
	`ep_group_seq`  varchar(100)   ,
	`ep_grroup_name`  varchar(100)   ,
	`ep_group_color`  varchar(100)   ,
	`ep_order`  int   ,
	`delete_yn`  char(1)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( ep_group_seq )
);

create table cms_ldapserver(
	`id`  varchar(100)   ,
	`title`  varchar(100)   ,
	`password`  varchar(100)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( id )
);

create table cms_resv_cospace(
	`resv_seq`  int   ,
	`start_date`  datetime   ,
	`resv_name`  varchar(100)   ,
	`end_date`  datetime   ,
	`passcode`  varchar(100)   ,
	`call_id`  varchar(100)   ,
	`bandwidth`  varchar(100)   ,
	`delete_yn`  char(1)   ,
	`use_yn`  char(1)   ,
	`call_yn`  char(1)   ,
	`discon_yn`  char(1)   ,
	`call_uuid`  varchar(300)   ,
	`cospace_uuid`  varchar(300)   ,
	`schedule_call_type`  varchar(50)   ,
	`host_name`  varchar(300)   ,
	`host_email`  varchar(100)   ,
	`cospace_type`  varchar(100)   ,
	`cospace_url`  varchar(2000)   ,
	`duration`  int   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( resv_seq )
);

create table cms_resv_cospace_endpoint(
	`resv_seq`  int   ,
	`ep_id`  int   ,
	`call_yn`  char(1)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( resv_seq, ep_id )
);

create table cms_resv_cospace_user(
	`resv_seq`  int   ,
	`userjid`  varchar(200)   ,
	`name`  varchar(200)   ,
	`email`  varchar(200)   ,
	`call_yn`  char(1)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( resv_seq, userjid )
);

create table cms_template(
	`seq`  int   ,
	`title`  varchar(100)   ,
	`delete_yn`  char(1)   ,
	`callbrandingprofile`  varchar(100)   ,
	`calllegprofile`  varchar(100)   ,
	`callprofile`  varchar(100)   ,
	`dtmfprofile`  varchar(100)   ,
	`ivrbrandingprofile`  varchar(100)   ,
	`userprofile`  varchar(100)   ,
	`note`  varchar(1000)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( seq )
);

create table cms_code_group(
	`group_code`  varchar(20)   ,
	`group_name`  varchar(100)   ,
	`group_ename`  varchar(100)   ,
	`group_note`  varchar(500)   ,
	`delete_yn`  char(1)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( group_code )
);

create table cms_code_detail(
	`group_code`  varchar(20)   ,
	`detail_code`  varchar(20)   ,
	`code_name`  varchar(100)   ,
	`code_ename`  varchar(100)   ,
	`note`  varchar(500)   ,
	`ref_code`  varchar(20)   ,
	`order_no`  int   ,
	`delete_yn`  char(1)   ,
	`regist_date`  datetime   ,
	`regist_id`  varchar(50)   ,
	`modify_date`  datetime   ,
	`modify_id`  varchar(50)   ,
	primary key ( group_code, detail_code )
);

create table cms_login_log(
	`seq`  int  auto_increment ,
	`user_id`  char(8)   ,
	`login_ip`  varchar(20)   ,
	`user_agent`  varchar(100)   ,
	`regist_date`  datetime   ,
	primary key ( seq )
);
