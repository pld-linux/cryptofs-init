Summary:	Encrypted filesystems support for rc-scripts
Summary(pl):	Wsparcie dla szyfrowanych systemów plików do skryptów startowych
Name:		cryptofs-init
Version:	1.4
Release:	2
License:	GPL
Group:		Base
Source0:	ftp://ftp.pld-linux.org/software/cryptofs-init/%{name}-%{version}.tar.gz
# Source0-md5:	650fa5aeb21e8fa62aa7f7b1d76c7a26
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	losetup >= 2.11g-3
Requires:	mount
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of scripts to provide easy set up and
usage of encrypted filesystems and swap space.

%description -l pl
Ten pakiet zawiera zestaw skryptów zapewniaj±cy ³atwe ustawienie i
u¿ytkowanie szyfrowanych systemów plików oraz plików/partycji wymiany

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add cryptofs

%postun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del cryptofs
fi

%files
%defattr(644,root,root,755)
%doc modules.conf cryptofstab.example README
%verify(not size mtime md5) %config(noreplace) %{_sysconfdir}/cryptofstab
%attr(754,root,root) /etc/rc.d/init.d/cryptofs*
