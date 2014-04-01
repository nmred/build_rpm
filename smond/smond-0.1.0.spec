Summary:swan mon beta
Name:smond
Version:0.1.0
Release:beta
Group:Development/Tools
License:BSD
URL:http://www.swanlinux.net
Vendor:swanteam <nmred_2008@126.com>
Packager:nmred <nmred_2008@126.com>
Distribution:Open source Project
Source:%{name}-%{version}.tar
Buildroot:%{_tmppath}/%{name}-%{version}
Prefix:/usr/local/swan/smond
Requires:chkconfig, sudo, nmap, libc-client
%define debug_packages %{nil}
%define debug_package %{nil}
%description
-------------------------------------
- Everything in order to facilitate -
-------------------------------------

%prep
%setup -q
%build

%pre
if grep -q swan /etc/passwd
then
	echo "Notice: Run this soft will use swan user"
else
	sudo adduser swan -s /sbin/nologin
fi
if test -d %{prefix}; then
	echo ""
	echo "Install dir \'%{prefix}\' exists. You need resolve it manually before install swansoft. Exit now."
	echo ""
# return !0 for exit.
	test ""
fi
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}
cp -r * $RPM_BUILD_ROOT%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# build install
echo ""
echo "Build: START"
chmod -R 755  %{prefix}/app
chmod -R 755  %{prefix}/tmp_install/sbin
if %{prefix}/tmp_install/sbin/build_install; then
	echo -e "Build: [0;32mDONE[0m"
else    
	echo -e "Build: [0;31mFAIL[0m"
fi
%preun
# stop smond
echo -n "Stop SMOND ... "
%{prefix}/tmp_install/sbin/stop_swansoft
echo "OK"
# backup cron config
mv /etc/cron.d/smond /usr/local/swan/smond/etc/sw_cron.crond.backup > /dev/null 2>&1
# del initd
/sbin/chkconfig --del smond > /dev/null 2>&1
# backup old version
SW_TMP_BAK_PATH=%{prefix}-backup-$(date +%%Y%%m%%d-%%H%%M%%S)
mv %{prefix} $SW_TMP_BAK_PATH
echo "Old version '%{prefix}' backup to '$SW_TMP_BAK_PATH'"
%postun
rm -f /etc/init.d/smond /usr/bin/smond
rm -f /etc/cron.d/smond
%files
%{prefix}

%changelog
*Tue Apr 01 2014 SWANTEAM <NMRED_2008@126.COM>

+ 添加 redis
+ 添加 mysql PDO 扩展
+ V0.1.0 首次 smeta.smond.swanweb 统一主版本号

*Fri Feb 21 2014 SWANTEAM <NMRED_2008@126.COM>

+ 建立监控器 


