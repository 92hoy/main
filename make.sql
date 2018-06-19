create table cms_manager(
	user_id varchar(50) primary key not null,
    user_name varchar(50)  not null,
    user_pwd varchar(100)  not null,
    user_role varchar(100)  not null,
    pw_change_date datetime default null,
    login_fail_cnt int default 0,
    last_login datetime default null,
    language varchar(20) default 'en',
    delete_yn char(1) default 'N',
    regist_date datetime default now(),
    regist_id varchar(50) default null,
    modify_date datetime default null,
    modify_id varchar(50) default null
);

insert into cms_manager(user_id, user_name, user_pwd, user_role)
values('system', '안진용', 'edx', 'S');

insert into cms_manager(user_id, user_name, user_pwd, user_role)
values('admin', '조호영', 'edx', 'A');

insert into cms_manager(user_id, user_name, user_pwd, user_role)
values('user', '안이형', 'edx', 'U');

insert into cms_manager(user_id, user_name, user_pwd, user_role)
values('monitor', '이원도', 'edx', 'M');
