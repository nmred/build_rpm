Summary:dev for swansoft beta
Name:dev_swan
Version:0.2.0
Release:beta
Group:Development/Tools
License:BSD
URL:http://www.swanlinux.net
Vendor:swanteam <nmred_2008@126.com>
Packager:nmred <nmred_2008@126.com>
Distribution:Open source Project
Source:%{name}-%{version}.tar
Buildroot:%{_tmppath}/%{name}-%{version}
Prefix:/usr/local/dev_swan
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
# stop swan_soft
echo -n "Stop SWANSOFT ... "
%{prefix}/tmp_install/sbin/stop_swansoft
echo "OK"
# backup cron config
mv /etc/cron.d/swan_soft /usr/local/swan/opt/etc/sw_cron.crond.backup > /dev/null 2>&1
# del initd
/sbin/chkconfig --del swan_soft > /dev/null 2>&1
# backup old version
SW_TMP_BAK_PATH=%{prefix}-backup-$(date +%%Y%%m%%d-%%H%%M%%S)
mv %{prefix} $SW_TMP_BAK_PATH
echo "Old version '%{prefix}' backup to '$SW_TMP_BAK_PATH'"
%postun
rm -f /etc/init.d/swan_soft /usr/bin/swan_soft
rm -f /etc/cron.d/swan_soft
%files
%{prefix}

%changelog
*Fri Mar 29 2013 SWANTEAM <NMRED_2008@126.COM>

+ 修正开发环境中php没有pdo-mysql相关的模块的bug
